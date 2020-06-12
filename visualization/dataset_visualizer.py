import csv
import matplotlib.pyplot as plt
from helpers import dataset_parser as parser
from similarities.lcs import LCSSimilarity
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
    """Plot length distribution histogram from a list of lengths and a list of labels."""

    hist_all(x)
    hist_positive(x, y)
    plt.show()


def visualize_len_from_file(filename):
    """Plot length distribution histogram."""
    
    pairs, _ = parser.dataset_from_file(filename)
    comments = [pair[0] for pair in pairs] + [pair[1] for pair in pairs]
    x = list(map(len, comments))
    hist_all(x)
    plt.show()


if __name__ == '__main__':
    visualize_len_from_file('datasets/dataset.csv')
