from sklearn.linear_model import LogisticRegression
from helpers import dataset_parser
import difflib
import numpy as np


def get_name(signature):
    """Extract object name from its signature."""

    words = signature.split()
    if words[0] == '#':
        words = words[1:]
    object_type = words[0]
    if object_type == 'Method':
        for word in words:
            if '(' in word:
                return word.split('(')[0]
    else:
        return words[1]


def get_signature_similarities(signature_pairs):
    """Get char LCS similarity for each signature pair."""

    return [difflib.SequenceMatcher(None, sig1, sig2).ratio() for sig1, sig2 in signature_pairs]


def get_lengths(pairs):
    """Get sum of lengths for each comment pair."""

    return [len(c1) + len(c2) for c1, c2 in pairs]


def extract_features(data, similarity):
    """Get a list of features (X) and a list of labels (y)."""

    data = np.array(data)
    pairs = data[:, :2]
    labels = data[:, 2]

    signatures1 = [get_name(sig) for sig in data[:, 3]]
    signatures2 = [get_name(sig) for sig in data[:, 4]]
    signature_similarities = get_signature_similarities(list(zip(signatures1, signatures2)))

    comment_lengths = get_lengths(pairs)

    similarities = similarity.run_similarity(pairs)

    return np.array(list(zip(similarities, comment_lengths, signature_similarities))), np.array(labels)


def logistic_regression_train(data, similarity):
    X, y = extract_features(data, similarity)
    model = LogisticRegression().fit(X, y)
    return model


def logistic_regression_boundary(model):
    coefs = model.coef_[0]
    bias = model.intercept_[0]
    return coefs, bias
