from helpers import dataset_parser as parser
from random import sample


def randomized_filter(file_in, file_out):
    """Sample a subset of the negative class from the input dataset of a size 
    of the positive class and write both classes to the output file."""

    data = parser.list_from_file(file_in)
    data_neg = list(filter(lambda x: x[2] == '0', data))
    data_pos = list(filter(lambda x: x[2] == '1', data))

    size = len(data_pos)
    data_neg_filtered = sample(data_neg, size)
    parser.list_to_file(data_pos + data_neg_filtered, file_out)


def print_statistics(filename):
    """Print dataset and class sizes."""

    data = parser.list_from_file(filename)
    print('Filename:', filename)
    print('Dataset size:', len(data))
    data_neg = list(filter(lambda x: x[2] == '0', data))
    data_pos = list(filter(lambda x: x[2] == '1', data))
    print('Negative class:', len(data_neg))
    print('Positive class:', len(data_pos))
