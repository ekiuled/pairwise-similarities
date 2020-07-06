from similarities.similarity import Similarity
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix, precision_score
from sklearn.model_selection import train_test_split
import pandas as pd


def train_test(func):
    def wrapper(train, test, similarity, verbose, name):
        df_train = pd.read_csv(train, index_col=0)
        x_train = list(zip(df_train.comment1, df_train.comment2))
        y_train = df_train.label.tolist()

        df_test = pd.read_csv(test, index_col=0)
        x_test = list(zip(df_test.comment1, df_test.comment2))
        y_test = df_test.label.tolist()

        similarity.train(x_train, y_train, verbose, name)
        y_pred = similarity.run_similarity(x_test)

        return func(similarity, y_test, y_pred)
    return wrapper


def test_set(func):
    def wrapper(test, similarity, name):
        df_test = pd.read_csv(test, index_col=0)
        x_test = list(zip(df_test.comment1, df_test.comment2))
        y_test = df_test.label.tolist()

        similarity.load(name)
        y_pred = similarity.run_similarity(x_test)

        return func(similarity, y_test, y_pred)
    return wrapper


def shuffled_test_set(func):
    def wrapper(filename, similarity, verbose, *args, **kwargs):
        df = pd.read_csv(filename, index_col=0)
        pairs = list(zip(df.comment1, df.comment2))
        labels = df.label.tolist()

        x_train, x_test, y_train, y_test = train_test_split(pairs, labels, test_size=0.2, random_state=42, stratify=labels)
        similarity.train(x_train, y_train, verbose)
        y_pred = similarity.run_similarity(x_test)

        return func(similarity, y_test, y_pred, *args, **kwargs)
    return wrapper


def get_metrics(similarity, labels, scores):
    """Get Accuracy, F1, ROC AUC and confusion matrix elements."""

    predictions = similarity.predict(scores)
    cm = confusion_matrix(labels, predictions)
    true_positives = int(cm[1][1])
    true_negatives = int(cm[0][0])
    false_positives = int(cm[0][1])
    false_negatives = int(cm[1][0])
    return {'accuracy': accuracy_score(labels, predictions),
            'f1': f1_score(labels, predictions),
            'precision': precision_score(labels, predictions),
            'roc': roc_auc_score(labels, scores),
            'tp': true_positives,
            'tn': true_negatives,
            'fp': false_positives,
            'fn': false_negatives}
