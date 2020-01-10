from math import log
import dataset_parser as parser
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from logistic_regression import logistic_regression
import numpy as np


def plot_lr(filename, similarity, fig):
    lr = logistic_regression(filename, similarity,
                             extra_features=True, show_metrics=True)

    w = lr.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(0, 1)
    yy = a * xx - (lr.intercept_[0]) / w[1]

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


def plot_dataset(sims, lenghts, groups, fig):
    n_bins = get_bins(len(sims))

    sims_pos = list(map(lambda x: x[0], list(
        filter(lambda x: x[1] == '1', zip(sims, groups)))))
    lenghts_pos = list(map(lambda x: x[0], list(
        filter(lambda x: x[1] == '1', zip(lenghts, groups)))))

    fig.add_trace(go.Scatter(
        x=sims_pos,
        y=lenghts_pos,
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

    sims_neg = list(map(lambda x: x[0], list(
        filter(lambda x: x[1] == '0', zip(sims, groups)))))
    lenghts_neg = list(map(lambda x: x[0], list(
        filter(lambda x: x[1] == '0', zip(lenghts, groups)))))

    fig.add_trace(go.Scatter(
        x=sims_neg,
        y=lenghts_neg,
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
        height=800,
        width=800,
    )

    return fig


def visualize_data_and_lr_decision_boundary(filename, similarity):
    pairs, groups = parser.dataset_from_file(filename)
    lengths = list(map(lambda x: (len(x[0]) + len(x[1]))*0.5, pairs))
    sims = similarity.run_similarity(pairs)

    fig = go.Figure()
    #fig = hist3d(sims, lengths, fig)
    fig = plot_dataset(sims, lengths, groups, fig)
    fig = plot_lr(filename, similarity, fig)
    fig.update_yaxes(range=[0, 2000])
    fig.show()