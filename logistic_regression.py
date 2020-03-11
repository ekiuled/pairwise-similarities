from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold
import sklearn.metrics as metrics

from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
from similarities.lsh_similarity import LSHSimilarity
import dataset_parser as parser

import numpy as np


class Model():
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

    def j_k_fold_cv(self, pairs, groups, scoring='f1', j=4, k=5):
        """Performs J-K-fold CV and returns a list of J scores."""

        X = self.get_features_extra(pairs)
        y = list(map(int, groups))
        scores = []
        for _ in range(j):
            scores.append(np.mean(cross_validate(
                LogisticRegression(), X, y, scoring=scoring, cv=StratifiedKFold(n_splits=k, shuffle=True))['test_score']))
        return scores

    def cross_validate(self, pairs, groups, scoring='f1'):
        """Performs a single run of K-fold CV and returns a list of scores."""

        X = self.get_features_extra(pairs)
        y = list(map(int, groups))
        return cross_validate(LogisticRegression(), X, y, scoring=scoring)['test_score']

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

        self.model = LogisticRegression().fit(x_train, y_train)

        if show_metrics or return_metrics:
            y_pred = self.model.predict(x_test)

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

        w = self.model.coef_[0]
        a = -w[0] / w[1]
        return [a, -(self.model.intercept_[0]) / w[1]]

    def predict(self, pairs):
        x = self.get_features_extra(pairs)
        y = self.model.predict(x)
        return y


if __name__ == "__main__":
    pairs, groups = parser.dataset_from_file('filtered.csv')
    for vectorized in [False, True]:
        print('Vectorized =', vectorized)
        for name, similarity in zip(['LCS', 'COS', 'Lev', 'LSH'], [LCSSimilarity(vectorized=vectorized), COSSimilarity(vectorized=vectorized), LevenshteinSimilarity(vectorized=vectorized), LSHSimilarity(vectorized=vectorized)]):
            model = Model(similarity)
            scores = model.j_k_fold_cv(pairs, groups)
            print('%s F1: %0.3f (+/- %0.3f)' % (name, np.mean(scores), np.std(scores) * 2))
            #scores = model.cross_validate(pairs, groups)
            #print('%s F1: %0.3f (+/- %0.32f)' % (name, np.mean(scores), np.std(scores) * 2))

