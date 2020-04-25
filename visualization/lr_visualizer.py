from math import log
import dataset_parser as parser
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from logistic_regression import Model
from sklearn.model_selection import train_test_split
import numpy as np
from random import sample
from timeit import default_timer as timer


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


def plot_error(pairs, groups, similarity, name, fig, score='f1', range_ub=2000):
    sizes = list(range(100, min(len(pairs), range_ub), 100))
    scores = []
    model = Model(similarity)
    pairs, groups = model.get_numeric(pairs, groups)

    for n in sizes:
        p, _, g, _ = train_test_split(
            pairs, groups, train_size=n)
        m = np.mean(model.j_k_fold_cv(p, g, scoring=score, numeric=True))
        scores.append(m)

    fig.add_trace(go.Scatter(
        x=sizes,
        y=scores,
        mode='lines+markers',
        name=name,
        hovertemplate='<b>' + name +
        '</b><br>Size: %{x}<br>Metric: %{y:.4f} <extra></extra>'
    ))

    return fig


def plot_time(pairs, similarity, name, fig, range_ub=2000):
    sizes = list(range(100, min(len(pairs), range_ub), 200))
    scores = []

    for n in sizes:
        p = sample(pairs, n)
        start = timer()
        similarity.run_similarity(p)
        end = timer()
        scores.append(end - start)

    fig.add_trace(go.Scatter(
        x=sizes,
        y=scores,
        mode='lines+markers',
        name=name,
        hovertemplate='<b>' + name +
        '</b><br>Size: %{x}<br>Time: %{y:.3f}s<extra></extra>'
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


def visualize_error(filename, similarities, names, score='f1', title='', height=900, width=1100):
    scores = {'f1', 'neg_log_loss', 'precision', 'recall'}
    if score not in scores:
        raise ValueError(
            "visualize_error: score must be one of %r." % scores)

    pairs, groups = parser.dataset_from_file(filename)
    fig = go.Figure()
    for similarity, name in zip(similarities, names):
        fig = plot_error(pairs, groups, similarity, name, fig, score)

    fig.update_layout(
        title=title,
        xaxis_title='Dataset size',
        yaxis_title=score,
        height=height,
        width=width,
    )
    fig.show()


def visualize_time(filename, similarities, names, height=900, width=1100):
    pairs, _ = parser.dataset_from_file(filename)
    fig = go.Figure()

    for similarity, name in zip(similarities, names):
        fig = plot_time(pairs, similarity, name, fig)
    
    fig.update_layout(
            xaxis_title='Dataset size',
            yaxis_title='Time in seconds',
            height=height,
            width=width,
        )
    fig.show()
