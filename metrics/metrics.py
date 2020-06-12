from helpers import similarity_generator, dataset_parser
from similarities.similarity import Similarity
from sklearn.metrics import accuracy_score, f1_score, roc_curve, auc
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
        return func(labels, scores, *args, **kwargs)
    return wrapper


def test_set(func):
    def wrapper(filename, similarity, *args, **kwargs):
        pairs, labels = dataset_parser.dataset_from_file(filename)
        x_train, x_test, y_train, y_test = train_test_split(pairs, labels, test_size=0.1, random_state=42, stratify=labels)
        if hasattr(similarity, 'train'):
            similarity.train(x_train, y_train)
        y_pred = similarity.run_similarity(x_test)
        return func(y_test, y_pred, *args, **kwargs)
    return wrapper


@test_set
def get_metrics(labels, scores, metric):
    """Get metric and optimal threshold."""

    fpr, tpr, thresholds = roc_curve(labels, scores)

    if metric == 'roc':
        optimal_ix = np.argmax(tpr - fpr)
        return auc(fpr, tpr), thresholds[optimal_ix]
    elif metric == 'accuracy' or metric == 'f1':
        metrics = []
        metric_func = accuracy_score if metric == 'accuracy' else f1_score
        for threshold in thresholds:
            predictions = np.greater_equal(scores, threshold).astype(int)
            metrics.append(metric_func(labels, predictions))
        optimal_ix = np.argmax(metrics)
        return metrics[optimal_ix], thresholds[optimal_ix]
    else:
        raise ValueError('`metric` must be roc, accuracy or f1.')
