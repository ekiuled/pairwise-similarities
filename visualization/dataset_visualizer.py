import csv
import matplotlib.pyplot as plt
import dataset_parser as parser
from similarities.lcs_similarity import LCSSimilarity
from math import log


def get_bins(n):
    return int(1 + 3.2 * log(n))


def hist_positive(x, y):
    data_pos = list(map(lambda x: x[0], list(filter(lambda x: x[1] == '1', zip(x, y)))))
    n_bins = get_bins(len(x))
    plt.hist(data_pos, n_bins, fc=(0, 0, 1, 0.5))


def hist_all(x):
    n_bins = get_bins(len(x))
    plt.hist(x, n_bins, fc=(0, 1, 0, 0.5))


def visualize(x, y):
    hist_all(x)
    hist_positive(x, y)
    plt.show()


def visualize_from_file(filename):
    """Plots a histogram of LCS similarity distribution."""

    pairs, y = parser.dataset_from_file(filename)
    similarity = LCSSimilarity()
    x = similarity.run_similarity(pairs)
    visualize(x, y)


def visualize_len_from_file(filename):
    """Plots a histogram of lenght distribution."""
    
    pairs, _ = parser.dataset_from_file(filename)
    comments = [pair[0] for pair in pairs] + [pair[1] for pair in pairs]
    x = list(map(len, comments))
    hist_all(x)
    plt.show()


if __name__ == '__main__':
    visualize_len_from_file('dataset.csv')