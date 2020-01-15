from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics

from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
import dataset_parser as parser

import numpy as np


def get_features(pairs, similarity):
    """Extracts similarity features and ground truth target values from a csv file."""

    x = similarity.run_similarity(pairs)
    x = np.reshape(x, (-1, 1))
    return x


def get_features_extra(pairs, similarity):
    """Extracts similarity and lenght features and ground truth target values from a csv file."""

    similarities = similarity.run_similarity(pairs)
    x = []
    for pair, sim in zip(pairs, similarities):
        l1, l2 = len(pair[0]), len(pair[1])
        x.append([sim, l1 + l2])
        # x.append([sim, min(l1, l2), max(l1, l2)])
    return x


def logistic_regression(pairs, groups, similarity, extra_features=False, show_metrics=False, return_metrics=False):
    """Performs logistic regression with chosen similarity method as a feature and returns the classifier and metrics.
    
    Returns
    -------
    [lr, m]
        List of logistic regression classifier and computed F1 score. 
    """

    x = get_features_extra(
        pairs, similarity) if extra_features else get_features(pairs, similarity)
    y = groups
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

    lr = LogisticRegression().fit(x_train, y_train)

    if show_metrics or return_metrics:
        y_pred = lr.predict(x_test)

        if show_metrics:
            print('Precision:', metrics.precision_score(
                y_test, y_pred, pos_label='1'))
            print('Recall:', metrics.recall_score(y_test, y_pred, pos_label='1'))
            print('F1 score:', metrics.f1_score(y_test, y_pred, pos_label='1'))

        if return_metrics:
            return [lr, metrics.f1_score(y_test, y_pred, pos_label='1')]

    return [lr]


if __name__ == "__main__":
    #parser.cache_similarity_to_file('filtered.csv', 'filtered_lcs.csv', LCSSimilarity())
    pairs, groups = parser.dataset_from_file('filtered.csv')
    logistic_regression(pairs, groups, LCSSimilarity(),
                        extra_features=False, show_metrics=True)
    # test('filtered.csv', COSSimilarity())
    # test('filtered.csv', LevenshteinSimilarity())
