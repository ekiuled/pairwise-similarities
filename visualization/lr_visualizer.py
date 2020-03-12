from math import log
import dataset_parser as parser
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from logistic_regression import Model
from sklearn.model_selection import train_test_split
import numpy as np


def plot_lr(pairs, groups, similarity, fig):
    model = Model(similarity)
    model.train(pairs, groups, show_metrics=True)

    a, b = model.coef()
    xx = np.linspace(0, 1)
    yy = a * xx + b

    fig.add_trace(go.Scatter(
        x=xx,
        y=yy,
        mode="lines",
        name='decision boundary',
        line=go.scatter.Line(color="gray"),
        showlegend=False
    ))

    return fig


def get_bins(n):
    return int(1 + 3.2 * log(n))


def hist3d(sims, lengths, fig):
    n_bins = get_bins(len(sims))

    fig.add_trace(go.Histogram2d(
        x=sims,
        y=lengths,
        colorscale='YlGnBu',
        zmax=10,
        nbinsx=n_bins,
        nbinsy=n_bins,
        zauto=False,
    ))

    fig.update_layout(
        xaxis_title="Similarities",
        yaxis_title="Average lenght",
        height=800,
        width=800,
    )

    return fig


def plot_dataset(pairs, groups, similarity, fig):
    pairs_pos = list(map(lambda x: x[0], list(
        filter(lambda x: x[1] == '1', zip(pairs, groups)))))
    sims_pos = similarity.run_similarity(pairs_pos)
    lenghts_pos = list(map(lambda x: (len(x[0]) + len(x[1]))*0.5, pairs_pos))

    fig.add_trace(go.Scatter(
        x=sims_pos,
        y=lenghts_pos,
        text=list(map(lambda x: x[0] + '<br>' + x[1], pairs_pos)),
        mode='markers',
        name='positive',
        showlegend=False,
        marker=dict(
            symbol='x',
            opacity=0.7,
            color='blue',
            size=8,
            line=dict(width=1),
        )
    ))

    pairs_neg = list(map(lambda x: x[0], list(
        filter(lambda x: x[1] == '0', zip(pairs, groups)))))
    sims_neg = similarity.run_similarity(pairs_neg)
    lenghts_neg = list(map(lambda x: (len(x[0]) + len(x[1]))*0.5, pairs_neg))

    fig.add_trace(go.Scatter(
        x=sims_neg,
        y=lenghts_neg,
        text=list(map(lambda x: x[0] + '<br>' + x[1], pairs_neg)),
        mode='markers',
        name='negative',
        showlegend=False,
        marker=dict(
            symbol='circle',
            opacity=0.7,
            color='red',
            size=8,
            line=dict(width=1),
        )
    ))

    fig.update_layout(
        xaxis_title="Similarities",
        yaxis_title="Average lenght",
        height=900,
        width=1000,
    )

    return fig


def plot_error(pairs, groups, similarity, name, fig, error='f1', range_ub=2000):
    sizes = list(range(100, min(len(pairs), range_ub), 100))
    errors = []
    model = Model(similarity)
    pairs, groups = model.get_numeric(pairs, groups)

    for n in sizes:
        p, _, g, _ = train_test_split(
            pairs, groups, train_size=n)
        m = np.mean(model.j_k_fold_cv(p, g, numeric=True))
        errors.append(m)

    fig.add_trace(go.Scatter(
        x=sizes,
        y=errors,
        mode='lines+markers',
        name=name
    ))

    return fig


def visualize_data_and_lr_decision_boundary(filename, similarity):
    pairs, groups = parser.dataset_from_file(filename)

    fig = go.Figure()
    #fig = hist3d(sims, lengths, fig)
    fig = plot_dataset(pairs, groups, similarity, fig)
    fig = plot_lr(pairs, groups, similarity, fig)
    fig.update_yaxes(range=[0, 2000])
    fig.show()


def visualize_error(filename, similarities, names, error='f1', title=''):
    errors = {'f1', 'log_loss'}
    if error not in errors:
        raise ValueError(
            "visualize_error: error must be one of %r." % errors)

    pairs, groups = parser.dataset_from_file(filename)
    fig = go.Figure()
    for similarity, name in zip(similarities, names):
        fig = plot_error(pairs, groups, similarity, name, fig, error)

    fig.update_layout(
        title=title,
        xaxis_title='Dataset size',
        yaxis_title=error,
    )
    fig.show()
