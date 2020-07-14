from helpers import dataset_parser
from helpers.similarity_generator import all_algorithms, get_algorithm_by_name
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix
from tabulate import tabulate
import pandas as pd
import numpy as np
from pipeline import ml


def label_unlabeled(file_in, file_out_prefix='data/up/'):
    """Get all unlabeled pairs from `file_in` and save those predicted as positives in `file_out`.
    Sort by predictions."""

    table = []
    headers = ['Algorithm', 'UP']
    df = pd.read_csv(file_in, index_col=0, na_filter=False)

    for name in ['LCS', 'COS', 'LEV', 'LSH', 'WMD']:
        alg = get_algorithm_by_name(name, True)
        model = ml.logistic_regression_train('data/train.csv', alg)
        X, _ = ml.extract_features(file_in, alg)

        predictions = model.predict(X)
        scores = model.predict_proba(X)
        scores = scores[predictions == 1]
        scores = scores[:, 1]
        df_up = df[predictions == 1]
        df_up.drop(columns=['label', 'name1', 'name2'], inplace=True)
        df_up.insert(4, 'score', scores)
        df_up.sort_values(by='score', ascending=False, inplace=True)
        df_up.to_csv(file_out_prefix + 'scores/' + name + '.csv')
        table.append((name, len(df_up.index)))

    name = 'SiamX'
    alg = get_algorithm_by_name(name, True)
    scores = alg.run_similarity(df)
    predictions = alg.predict(scores)
    scores = scores[predictions == 1]
    df_up = df[predictions == 1]
    df_up.drop(columns=['label', 'name1', 'name2'], inplace=True)
    df_up.insert(4, 'score', scores)
    df_up.sort_values(by='score', ascending=False, inplace=True)
    df_up.to_csv(file_out_prefix + 'scores/' + name + '.csv')
    table.append((name, len(df_up.index)))

    print(tabulate(table, headers, tablefmt='grid'))


def label_unlabeled_plain(file_in, file_out_prefix='data/up/plain/'):
    """Get all unlabeled pairs from `file_in` and save those predicted as positives in `file_out`.
    Sort by predictions."""

    table = []
    headers = ['Algorithm', 'UP']
    df = pd.read_csv(file_in, index_col=0, na_filter=False)
    X = list(zip(df.comment1, df.comment2))

    for name, alg in all_algorithms():
        alg.load(name)

        scores = np.array(alg.run_similarity(X))
        predictions = alg.predict(scores)
        scores = scores[predictions == 1]
        df_up = df[predictions == 1]
        df_up.drop(columns=['label', 'name1', 'name2'], inplace=True)
        df_up.insert(4, 'score', scores)
        df_up.sort_values(by='score', ascending=False, inplace=True)
        df_up.to_csv(file_out_prefix + 'scores/' + name + '.csv')
        table.append((name, len(df_up.index)))

    print(tabulate(table, headers, tablefmt='grid'))


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
