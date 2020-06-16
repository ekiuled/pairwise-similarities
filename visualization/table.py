from metrics.unlabeled import compare_results
from metrics import metrics
from helpers.similarity_generator import all_algorithms
from tabulate import tabulate

table = []
headers = ['Algorithm', 'Accuracy', 'F1', 'ROC', 'TP', 'TN', 'FP', 'FN', 'UP', 'UN']

for name, alg in all_algorithms():
    labeled = metrics.test_set(metrics.get_metrics)('datasets/test.csv', alg, name)
    unlabeled = compare_results('datasets/test_full.csv', alg, name)
    table.append((name, labeled['accuracy'], labeled['f1'], labeled['roc'],
                  labeled['tp'], labeled['tn'], labeled['fp'], labeled['fn'],
                  unlabeled['up'], unlabeled['un']))

print(tabulate(table, headers, tablefmt='grid', floatfmt='.4f'))
