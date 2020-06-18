from helpers import dataset_parser
from similarities.similarity import Similarity
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np


def cached(func):
    def wrapper(filename, *args, **kwargs):
        scores, labels = dataset_parser.get_cache_from_file(filename)
        return func(labels, scores, *args, **kwargs)
    return wrapper


def calculated(func):
    def wrapper(filename, similarity, *args, **kwargs):
        pairs, labels = dataset_parser.dataset_from_file(filename)
        scores = similarity.run_similarity(pairs)
        return func(similarity, labels, scores, *args, **kwargs)
    return wrapper


def train_test(func):
    def wrapper(train, test, similarity, verbose, name):
        x_train, y_train = dataset_parser.dataset_from_file(train)
        x_test, y_test = dataset_parser.dataset_from_file(test)
        similarity.train(x_train, y_train, verbose, name)
        y_pred = similarity.run_similarity(x_test)
        return func(similarity, y_test, y_pred)
    return wrapper


def test_set(func):
    def wrapper(test, similarity, name):
        x_test, y_test = dataset_parser.dataset_from_file(test)
        similarity.load(name)
        y_pred = similarity.run_similarity(x_test)
        return func(similarity, y_test, y_pred)
    return wrapper


def shuffled_test_set(func):
    def wrapper(filename, similarity, verbose, *args, **kwargs):
        pairs, labels = dataset_parser.dataset_from_file(filename)
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
            'roc': roc_auc_score(labels, scores),
            'tp': true_positives,
            'tn': true_negatives,
            'fp': false_positives,
            'fn': false_negatives}
