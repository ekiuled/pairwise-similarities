from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold
import sklearn.metrics as metrics

from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
from similarities.lsh_similarity import LSHSimilarity
import dataset_parser as parser

import numpy as np
import scipy.stats as st


class Model():
    def __init__(self, similarity, extra_features=False):
        self.similarity = similarity
        self.extra_features = extra_features

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

    def get_numeric(self, pairs, groups):
        """Extracts features from pairs and transforms labels to integers."""

        return self.get_features_extra(pairs) if self.extra_features else self.get_features(pairs), list(map(int, groups))

    def j_k_fold_cv(self, pairs, groups, scoring='f1', j=4, k=5, numeric=False):
        """Performs J-K-fold CV and returns a list of J scores."""

        X, y = [np.reshape(pairs, (-1, 1)),
                groups] if numeric else self.get_numeric(pairs, groups)
        scores = []
        for _ in range(j):
            scores.append(np.mean(cross_validate(
                LogisticRegression(), X, y, scoring=scoring, cv=StratifiedKFold(n_splits=k, shuffle=True))['test_score']))
        return scores

    def cross_validate(self, pairs, groups, scoring='f1', numeric=False):
        """Performs a single run of K-fold CV and returns a list of scores."""

        X, y = [np.reshape(pairs, (-1, 1)),
                groups] if numeric else self.get_numeric(pairs, groups)
        return cross_validate(LogisticRegression(), X, y, scoring=scoring)['test_score']

    def train(self, pairs, groups, show_metrics=False, return_metrics=False):
        """Trains logistic regression and returns the metrics.

        Returns
        -------
        [m]
            List of computed metrics. 
        """

        x, y = self.get_numeric(pairs, groups)
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
                print('Accuracy:', metrics.accuracy_score(y_test, y_pred))

            if return_metrics:
                return [metrics.f1_score(y_test, y_pred), metrics.log_loss(y_test, y_pred), metrics.accuracy_score(y_test, y_pred)]

        return []

    def coef(self):
        """Decision boundary coefficients."""

        w = self.model.coef_[0]
        if len(w) == 1:
            a = 0
            b = -self.model.intercept_[0] / w[0]
        else:
            a = -w[0] / w[1]
            b = -(self.model.intercept_[0]) / w[1]
        return [a, b]

    def predict(self, pairs):
        x = self.get_features_extra(
            pairs) if self.extra_features else self.get_features(pairs)
        y = self.model.predict(x)
        return y


if __name__ == "__main__":
    pairs, groups = parser.dataset_from_file('data_clean.csv')
    sims = [COSSimilarity(True, None), LCSSimilarity(True, None), LSHSimilarity(
        True, None), LevenshteinSimilarity(False, None)]
    names = ['COS', 'LCS', 'LSH', 'Lev']

    for name, similarity in zip(names, sims):
        model = Model(similarity)
        scores = model.j_k_fold_cv(pairs, groups)
        interval = st.norm.interval(
            0.95, loc=np.mean(scores), scale=np.std(scores))
        print(
            f'{name} {np.mean(scores):.3f} +-{(interval[1] - interval[0])/2:.3f}')
