from logistic_regression import Model
import numpy as np
import scipy.stats as st
import roc
import similarity_generator
import dataset_parser as parser
from timeit import timeit
from random import sample


def print_metrics(scoring='f1'):
    def func(name, pairs, groups):
        scores = Model().j_k_fold_cv(
            pairs, groups, numeric=True, scoring=scoring)
        interval = st.norm.interval(
            0.95, loc=np.mean(scores), scale=np.std(scores))
        print(
            f'{np.mean(scores)*100:.2f}%±{(interval[1] - interval[0])/2*100:.2f}%')

    similarity_generator.map_cache(func)


def print_metrics_roc_auc():
    def func(name, pairs, groups):
        roc_auc = roc.get_auc(pairs, groups)
        print(f'{roc_auc:.5f}')

    similarity_generator.map_cache(func)


def print_time(filename):
    pairs, _ = parser.dataset_from_file(filename)
    pairs = sample(pairs, 100)

    def func(model, name):
        scores = []
        for p in pairs:
            scores.append(timeit(lambda: model.run_similarity([p]), number=1))
        interval = st.norm.interval(
            0.95, loc=np.mean(scores), scale=np.std(scores))
        print(
            f'{np.mean(scores)*1000:.3f}±{(interval[1] - interval[0])/2*1000:.3f}')

    similarity_generator.map(func)

    lenghts = []
    for p in pairs:
        lenghts.append(len(p[0]))
        lenghts.append(len(p[1]))
    interval = st.norm.interval(
        0.95, loc=np.mean(lenghts), scale=np.std(lenghts))
    print()
    print(
        f'{np.mean(lenghts):.2f}±{(interval[1] - interval[0])/2:.2f}')


def print_thresholds():
    def log_reg_threshold(pairs, groups):
        m = Model()
        m.train(pairs, groups, numeric=True)
        return m.coef()[1]

    def func(name, pairs, groups):
        print(f'{name} {log_reg_threshold(pairs, groups):.3f} {roc.get_optimal_threshold(pairs, groups):.3f}')

    similarity_generator.map_cache(func)


if __name__ == "__main__":
    print_time('data.csv')
