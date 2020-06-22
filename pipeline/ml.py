from sklearn.linear_model import LogisticRegression
from helpers import dataset_parser
import difflib
import numpy as np
import pandas as pd


def get_signature_similarities(signature_pairs):
    """Get char LCS similarity for each signature pair."""

    return [difflib.SequenceMatcher(None, sig1, sig2).ratio() for sig1, sig2 in signature_pairs]


def get_lengths(pairs):
    """Get sum of lengths for each comment pair."""

    return [len(c1) + len(c2) for c1, c2 in pairs]


def extract_features(filename, similarity):
    """Get a list of features (X) and a list of labels (y)."""

    df = pd.read_csv(filename, index_col=0)
    pairs = df[['comment1', 'comment2']]
    labels = df['label']

    names = df[['name1', 'name2']]
    name_similarities = get_signature_similarities(names.to_numpy())

    comment_lengths = get_lengths(pairs.to_numpy())

    similarities = similarity.run_similarity(pairs.to_numpy())

    return np.array(list(zip(similarities, comment_lengths, name_similarities))), labels.to_numpy()


def logistic_regression_train(filename, similarity):
    X, y = extract_features(filename, similarity)
    model = LogisticRegression().fit(X, y)
    return model


def logistic_regression_boundary(model):
    coefs = model.coef_[0]
    bias = model.intercept_[0]
    return coefs, bias
