from pipeline import ml
from helpers import dataset_parser, similarity_generator
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from metrics.metrics import get_metrics
import pandas as pd


def lr_evaluate(train_file, test_file, similarity, name):
    """Get metrics for logistic regression."""

    similarity.load(name)
    model = ml.logistic_regression_train(train_file, similarity)

    features, labels = ml.extract_features(test_file, similarity)
    predictions = model.predict(features)

    cm = confusion_matrix(labels, predictions)
    true_positives = int(cm[1][1])
    true_negatives = int(cm[0][0])
    false_positives = int(cm[0][1])
    false_negatives = int(cm[1][0])

    return {'accuracy': accuracy_score(labels, predictions),
            'f1': f1_score(labels, predictions),
            'tp': true_positives,
            'tn': true_negatives,
            'fp': false_positives,
            'fn': false_negatives}


def siamx_evaluate(train_file, test_file, verbose=False, train=False):
    """Get metrics for siamese neural network with extra feature."""

    df_train = pd.read_csv(train_file, index_col=0)
    df_test = pd.read_csv(test_file, index_col=0)

    name = 'SiamX'
    similarity = similarity_generator.get_algorithm_by_name(name)
    if train:
        similarity.train(df_train, verbose, name)
    else:
        similarity.load(name)
    y_pred = similarity.run_similarity(df_test)
    y_test = df_test['label'].to_numpy()

    return get_metrics(similarity, y_test, y_pred)
