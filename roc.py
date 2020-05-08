from similarities.cos_similarity import COSSimilarity
from similarities.lcs_similarity import LCSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
from similarities.lsh_similarity import LSHSimilarity
import dataset_parser as parser
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from numpy import argmax


def plot_roc_from_file(filename, similarity):
    pairs, groups = parser.dataset_from_file(filename)
    groups = list(map(int, groups))
    scores = similarity.run_similarity(pairs)
    plot_roc(scores, groups)


def plot_roc(scores, groups):
    fpr, tpr, thresholds = roc_curve(groups, scores)
    roc_auc = auc(fpr, tpr)
    optimal_ix = argmax(tpr - fpr)
    threshold = thresholds[optimal_ix]

    plt.plot(fpr, tpr, color='darkorange',
             label='ROC curve (area = %0.3f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', linestyle='--',
             label='ROC of a random classifier')
    plt.plot(fpr[optimal_ix], tpr[optimal_ix], marker='*',
             label='Optimal threshold %0.3f' % threshold)

    plt.xlim([-0.05, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()


def get_auc_from_file(filename, similarity):
    pairs, groups = parser.dataset_from_file(filename)
    groups = list(map(int, groups))
    scores = similarity.run_similarity(pairs)
    return get_auc(scores, [groups])


def get_auc(scores, groups):
    fpr, tpr, _ = roc_curve(groups, scores)
    return auc(fpr, tpr)


def get_optimal_threshold_from_file(filename, similarity):
    pairs, groups = parser.dataset_from_file(filename)
    groups = list(map(int, groups))
    scores = similarity.run_similarity(pairs)
    return get_optimal_threshold(scores, groups)


def get_optimal_threshold(scores, groups):
    fpr, tpr, thresholds = roc_curve(groups, scores)
    optimal_ix = argmax(tpr - fpr)
    return thresholds[optimal_ix]


if __name__ == '__main__':
    plot_roc('dataset.csv', LSHSimilarity())
    # for v in [False, True]:
    #     for n in [None, 'partial', 'full']:
    #         roc_auc = get_auc('dataset.csv', COSSimilarity(v, n))
    #         print('v =', v, ', n = ', n, ', ROC AUC =', f'{roc_auc: .4f}')
