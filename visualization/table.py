from metrics.unlabeled import compare_results
from metrics import metrics, logistic_regression_metrics
from helpers.similarity_generator import all_algorithms
from tabulate import tabulate


def similarity_metrics():
    table = []
    headers = ['Algorithm', 'Accuracy', 'F1', 'ROC', 'TP', 'TN', 'FP', 'FN', 'UP', 'UN']

    for name, alg in all_algorithms():
        labeled = metrics.test_set(metrics.get_metrics)('datasets/semi random split/test.csv', alg, name)
        table.append((name, labeled['accuracy'], labeled['f1'], labeled['roc'],
                      labeled['tp'], labeled['tn'], labeled['fp'], labeled['fn']))

    print(tabulate(table, headers, tablefmt='grid', floatfmt='.4f'))


def similarity_metrics_full_test():
    table = []
    headers = ['Algorithm', 'Accuracy', 'F1', 'ROC', 'TP', 'TN', 'FP', 'FN', 'UP', 'UN']

    for name, alg in all_algorithms():
        labeled = metrics.test_set(metrics.get_metrics)('datasets/test.csv', alg, name)
        unlabeled = compare_results('datasets/test_full.csv', alg, name)
        table.append((name, labeled['accuracy'], labeled['f1'], labeled['roc'],
                      labeled['tp'], labeled['tn'], labeled['fp'], labeled['fn'],
                      unlabeled['up'], unlabeled['un']))

    print(tabulate(table, headers, tablefmt='grid', floatfmt='.4f'))


def lr_test_metrics():
    table = []
    headers = ['Algorithm', 'Accuracy', 'F1', 'TP', 'TN', 'FP', 'FN']

    for name, alg in all_algorithms():
        labeled = logistic_regression_metrics.lr_evaluate('datasets/train.csv', 'datasets/test.csv', alg, name)
        table.append((name, labeled['accuracy'], labeled['f1'],
                      labeled['tp'], labeled['tn'], labeled['fp'], labeled['fn']))

    print(tabulate(table, headers, tablefmt='grid', floatfmt='.4f'))


def feature_metrics():
    table = []
    headers = ['Algorithm', 'Accuracy', 'LR Accuracy', 'F1', 'LR F1']

    for name, alg in all_algorithms():
        plain = metrics.test_set(metrics.get_metrics)('datasets/project split/test.csv', alg, name)
        lr = logistic_regression_metrics.lr_evaluate('datasets/project split/train.csv', 'datasets/project split/test.csv', alg, name)
        table.append((name, plain['accuracy'], lr['accuracy'],
                      plain['f1'], lr['f1']))

    print(tabulate(table, headers, tablefmt='grid', floatfmt='.4f'))


if __name__ == "__main__":
    similarity_metrics()
