from helpers import dataset_parser
from sklearn.metrics import confusion_matrix
from helpers.similarity_generator import all_algorithms
from tabulate import tabulate


def compare_results(train, test, similarity, cache=None):
    """Predict similarity on a partially labeled test set, cache results if `cache` name is set.
    Return several metrics."""

    x_train, y_train = dataset_parser.dataset_from_file(train)
    x_test, y_test = dataset_parser.dataset_from_file(test)
    similarity.train(x_train, y_train)
    y_pred = similarity.predict(similarity.run_similarity(x_test))
    cm = confusion_matrix(y_test, y_pred, [0, 1, -1])
    true_positives = cm[0][0]
    true_negatives = cm[1][1]
    false_positives = cm[0][1]
    false_negatives = cm[1][0]
    unlabeled_positives = cm[2][1]
    accuracy = (true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)
    f1 = 2*true_positives/(2*true_positives+false_positives+false_negatives)

    if cache:
        data = dataset_parser.list_from_file(test)
        data_pred = []
        for i in range(len(data)):
            if data[i][2] != '-1' or y_pred[i] == 1:
                data_pred.append(data[i] + [y_pred[i]])
        dataset_parser.list_to_file(data_pred, 'cache/' + cache + '.csv')

    return {'accuracy': accuracy,
            'f1': f1,
            'tp': true_positives,
            'tn': true_negatives,
            'fp': false_positives,
            'fn': false_negatives,
            'up': unlabeled_positives}


if __name__ == "__main__":
    table = []
    headers = ['Algorithm', 'Accuracy', 'F1', 'TP', 'TN', 'FP', 'FN', 'UP']

    for name, alg in all_algorithms():
        d = compare_results('datasets/train.csv', 'datasets/test_full.csv', alg, name)
        table.append([name] + list(d.values()))

    print(tabulate(table, headers, tablefmt='grid', floatfmt='.3f'))

    print()
    print(table)