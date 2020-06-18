from pipeline import ml
from helpers import dataset_parser, similarity_generator
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def lr_evaluate(train_file, test_file, similarity, name):
    """Get metrics for logistic regression."""

    train = dataset_parser.list_from_file(train_file)
    similarity.load(name)
    model = ml.logistic_regression_train(train, similarity)

    test = dataset_parser.list_from_file(test_file)
    features, labels = ml.extract_features(test, similarity)
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
