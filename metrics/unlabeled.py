from helpers import dataset_parser
from helpers.similarity_generator import all_algorithms
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
from tabulate import tabulate


def compare_results(test, similarity, cache=None):
    """Predict similarity on a partially labeled test set, cache results if `cache` name is set.
    Return several metrics."""

    x_test, y_test = dataset_parser.dataset_from_file(test)
    y_score = similarity.run_similarity(x_test)
    y_pred = similarity.predict(y_score)
    cm = confusion_matrix(y_test, y_pred, [0, 1, -1])
    true_positives = int(cm[1][1])
    true_negatives = int(cm[0][0])
    false_positives = int(cm[0][1])
    false_negatives = int(cm[1][0])
    unlabeled_positives = int(cm[2][1])
    unlabeled_negatives = int(cm[2][0])
    labels, scores, predictions = map(list, zip(*list(filter(lambda x: x[0] != -1, list(zip(y_test, y_score, y_pred))))))
    accuracy = accuracy_score(labels, predictions)
    f1 = f1_score(labels, predictions)
    roc = roc_auc_score(labels, scores)

    if cache:
        data = dataset_parser.list_from_file(test)
        data_pred = []
        for i in range(len(data)):
            if data[i][2] != '-1' or y_pred[i] == 1:
                data_pred.append(data[i] + [y_pred[i]])
        dataset_parser.list_to_file(data_pred, 'cache/' + cache + '.csv')

    return {'accuracy': accuracy,
            'f1': f1,
            'roc': roc,
            'tp': true_positives,
            'tn': true_negatives,
            'fp': false_positives,
            'fn': false_negatives,
            'up': unlabeled_positives,
            'un': unlabeled_negatives}
