from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics

from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
import dataset_parser as parser

import numpy as np


class Model:
    def __init__(self, similarity):
        self.similarity = similarity

    def get_features(self, pairs):
        """Extracts similarity features and ground truth target values from a csv file."""

        x = self.similarity.run_similarity(pairs)
        x = np.reshape(x, (-1, 1))
        return x

    def get_features_extra(self, pairs):
        """Extracts similarity and lenght features and ground truth target values from a csv file."""

        similarities = self.similarity.run_similarity(pairs)
        x = []
        for pair, sim in zip(pairs, similarities):
            l1, l2 = len(pair[0]), len(pair[1])
            x.append([sim, l1 + l2])
            # x.append([sim, min(l1, l2), max(l1, l2)])
        return x

    def train(self, pairs, groups, show_metrics=False, return_metrics=False):
        """Trains logistic regression and returns the metrics.

        Returns
        -------
        [m]
            List of computed metrics. 
        """

        x = self.get_features_extra(pairs)
        y = list(map(int, groups))
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, random_state=1)

        self.lr = LogisticRegression().fit(x_train, y_train)

        if show_metrics or return_metrics:
            y_pred = self.lr.predict(x_test)

            if show_metrics:
                print('Precision:', metrics.precision_score(y_test, y_pred))
                print('Recall:', metrics.recall_score(y_test, y_pred))
                print('F1 score:', metrics.f1_score(y_test, y_pred))
                print('Log loss:', metrics.log_loss(y_test, y_pred))

            if return_metrics:
                return [metrics.f1_score(y_test, y_pred), metrics.log_loss(y_test, y_pred)]

        return []

    def coef(self):
        """Decision boundary coefficients."""

        w = self.lr.coef_[0]
        a = -w[0] / w[1]
        return [a, -(self.lr.intercept_[0]) / w[1]]

    def predict(self, pairs):
        x = self.get_features_extra(pairs)
        y = self.lr.predict(x)
        return y


if __name__ == "__main__":
    #parser.cache_similarity_to_file('filtered.csv', 'filtered_lcs.csv', LCSSimilarity())
    pairs, groups = parser.dataset_from_file('filtered.csv')
    model = Model(LCSSimilarity())
    model.train(pairs, groups, show_metrics=True)
