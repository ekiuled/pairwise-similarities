from pipeline import ml
from helpers import similarity_generator, dataset_parser
import matplotlib.pyplot as plt
import numpy as np


def plot_dataset_and_boundary(filename, similarity, ax, model, ax_title):
    features, labels = ml.extract_features(filename, similarity)

    pos_features = features[labels == 1]
    neg_features = features[labels == 0]

    for f, m, l in [(pos_features, 'o', 'Positive class'), (neg_features, '^', 'Negative class')]:
        sims = f[:, 0]
        lengths = f[:, 1]
        sig_sims = f[:, 2]
        ax.scatter(sims, lengths, sig_sims, marker=m, label=l)

    coefs, bias = ml.logistic_regression_boundary(model)
    X = np.arange(0, 1, 0.05)
    Y_min = np.min(lengths) - 10
    Y_max = np.max(lengths) + 10
    Y = np.arange(Y_min, Y_max, (Y_max-Y_min)*.05)
    X, Y = np.meshgrid(X, Y)
    Z = (-coefs[0]*X - coefs[1]*Y - bias) / coefs[2]

    ax.plot_surface(X, Y, Z, color='purple', alpha=.1, edgecolors=(0.1, 0.2, 0.5, 0.2))
    ax.set_zlim(0, 1)

    ax.set_title(ax_title)
    ax.set_xlabel('Similarity')
    ax.set_ylabel('Length')
    ax.set_zlabel('Signature')
    ax.legend()


alg_name = 'LSH'
similarity = similarity_generator.get_algorithm_by_name(alg_name, True)

fig, (ax_train, ax_test) = plt.subplots(1, 2, subplot_kw=dict(projection='3d'))

model = ml.logistic_regression_train('data/train.csv', similarity)

plot_dataset_and_boundary('data/train.csv', similarity, ax_train, model, 'Train dataset')
plot_dataset_and_boundary('data/test.csv', similarity, ax_test, model, 'Test dataset')

fig.suptitle(alg_name)

plt.show()
