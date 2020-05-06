from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
from similarities.lsh_similarity import LSHSimilarity
from logistic_regression import Model
import dataset_parser as parser
import numpy as np
import scipy.stats as st
from roc import get_auc


def print_metrics(filename):
    models = [[] for _ in range(4)]
    names = []
    for vectorized in [False, True]:
        for normalized in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(vectorized, normalized))
            models[1].append(COSSimilarity(vectorized, normalized))
            models[2].append(LevenshteinSimilarity(vectorized, normalized))
            models[3].append(LSHSimilarity(vectorized, normalized))
            suffix = str(vectorized) + str(normalized)
            names.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, name in zip(algorithm, names):
            pairs, groups = parser.get_cache_from_file('cache/' + title + name)
            scores = Model(model).j_k_fold_cv(pairs, groups, numeric=True)
            interval = st.norm.interval(
                0.95, loc=np.mean(scores), scale=np.std(scores))
            print(
                f'{np.mean(scores)*100:.2f}%+-{(interval[1] - interval[0])/2*100:.2f}%')


def print_metrics_roc_auc(filename):
    models = [[] for _ in range(4)]
    names = []
    for vectorized in [False, True]:
        for normalized in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(vectorized, normalized))
            models[1].append(COSSimilarity(vectorized, normalized))
            models[2].append(LevenshteinSimilarity(vectorized, normalized))
            models[3].append(LSHSimilarity(vectorized, normalized))
            suffix = str(vectorized) + str(normalized)
            names.append(suffix)

    pairs, groups = parser.dataset_from_file(filename)
    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, name in zip(algorithm, names):
            pairs, groups = parser.get_cache_from_file('cache/' + title + name)
            roc_auc = get_auc(pairs, groups)
            print(f'{roc_auc: .5f}')


if __name__ == "__main__":
    print_metrics_roc_auc('dataset.csv')
