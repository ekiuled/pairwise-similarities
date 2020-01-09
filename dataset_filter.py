import dataset_parser as parser
import statistics
import dataset_visualizer as visualizer
from similarities.lcs_similarity import LCSSimilarity
import numpy as np
from scipy.stats import chisquare


def binned(data, num):
    n = len(data)
    n_bins = n // num
    delta = 1 / n_bins

    similarity = LCSSimilarity()
    similarities = similarity.run_similarity(data)

    def bin_fit(val, i, delta):
        return val >= i * delta and val < (i + 1) * delta

    return [[x[1] for x in zip(similarities, data) if bin_fit(x[0], i, delta)]
            for i in range(n_bins)]


def upper(data):
    data = data[len(data) // 2 + 1:]
    mean = statistics.mean(data)
    std = statistics.stdev(data)
    print('Mean:', mean, 'std:', std)
    bound = mean - std
    if bound > 0:
        return bound
    print('Negative upper bound, trying bigger...')
    return mean


def filter_negative_data(filename, num):
    data = parser.list_from_file(filename)
    data_neg = list(filter(lambda x: x[2] == '0', data))
    data_pos = list(filter(lambda x: x[2] == '1', data))

    bins = binned(data_neg, num)
    bound = int(upper(list(map(len, bins))))
    bins = list(map(lambda b: b[:bound], bins))
    return data_pos + [item for sublist in bins for item in sublist]


def filter_all_data(filename, num):
    data = parser.list_from_file(filename)
    bins = binned(data, num)
    bound = int(upper(list(map(len, bins))))
    bins = list(map(lambda b: b[:bound], bins))
    return [item for sublist in bins for item in sublist]


def chi_test(data, num):
    bins = binned(data, num)
    return chisquare(list(map(len, bins)))


def run_filter(file_in, file_out, num):
    filtered = filter_negative_data(file_in, num)
    parser.list_to_file(filtered, file_out)

    ## Гипотеза принимается, если pvalue > alpha
    #filtered = parser.list_from_file(file_out)
    chi_statistic, p_value = chi_test(filtered, num)
    print('Chi statistic & P value:', chi_statistic, p_value)
    print('Filtered count:', len(filtered))

    visualizer.visualize_from_file(file_out)


if __name__ == '__main__':
    # run_filter('data.csv', 'filtered.csv', 100)
    # run_filter('filtered.csv', 'filtered2.csv', 100)
    # visualizer.visualize_from_file('filtered.csv')
    visualizer.visualize_from_file('filtered.csv')
