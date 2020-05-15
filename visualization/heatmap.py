import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


def heatmap(title, save=False, show=True):
    f = open('stats/' + title + '.txt', 'r')
    labels = f.readlines()[:24]
    scores = [float(line.split('%')[0]) for line in labels]
    f.close()

    scores = np.transpose(np.reshape(scores, (4, -1)))
    labels = np.transpose(np.reshape(labels, (4, -1)))
    algs = ['LCS', 'COS', 'LEV', 'LSH']
    pipelines = ['Только алгоритм', 'Частичная нормализация', 'Полная нормализация',
                 'Сегментация', 'Сегм., частичная норм.', 'Сегм., полная норм.']

    fig, ax = plt.subplots(figsize=(16, 16))
    roffset = 0.8
    ax.imshow(scores, norm=colors.PowerNorm(gamma=2), cmap='coolwarm', aspect=0.4, alpha=0.7,
              extent=(-0.5+1+roffset, len(algs)-0.5+1+roffset, len(pipelines)-0.49+1, -0.49+1))

    for _, spine in ax.spines.items():
        spine.set_visible(False)

    ax.use_sticky_edges = False
    ax.margins(.01)
    ax.set_xticks(np.arange(len(algs)+1)-.5, minor=True)
    ax.set_yticks(np.arange(len(pipelines)+1)-.5, minor=True)
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.tick_params(axis='both', labelsize=18, left=False,
                   labelleft=False, bottom=False, labelbottom=False)

    ax.plot([-.5, -.5], [-0.5, len(pipelines)-0.49+1], color='k', linewidth=1)
    ax.plot([len(algs)-0.5+1+roffset, len(algs)-0.5+1+roffset],
            [-0.5, len(pipelines)-0.49+1], color='k', linewidth=1)
    ax.plot([-.5, len(algs)-0.5+1+roffset], [-.5, -.5], color='k', linewidth=1)
    ax.plot([-.5, len(algs)-0.5+1+roffset], [len(pipelines) -
                                             0.49+1, len(pipelines)-0.49+1], color='k', linewidth=1)

    ax.plot([-0.49, -0.5+1+roffset], [-0.49, -0.5+1], color='k', linewidth=1)
    ax.text(0.55, -.15, 'Алгоритмы', ha="left",
            va="center", color="k", fontsize=17)
    ax.text(-0.4, .1, 'Pipelines', ha="left",
            va="center", color="k", fontsize=17)

    for i in range(6):
        for j in range(4):
            ax.text(j+1+roffset, i+1.15,
                    labels[i][j], ha="center", va="center", color="k", fontsize=17)
    for j in range(4):
        ax.text(j+1+roffset, 0, algs[j], ha="center",
                va="center", color="k", fontsize=17)
        ax.plot([j+0.5+roffset, j+0.5+roffset],
                [-0.5, len(pipelines)-0.49+1], color='k', linewidth=1)
    for i in range(6):
        ax.text(-0.4, i+1, pipelines[i], ha="left",
                va="center", color="k", fontsize=17)
        ax.plot([-.5, len(algs)-0.5+1+roffset],
                [i+.5, i+.5], color='k', linewidth=1)

    if save:
        fig.savefig('stats/' + title + '.png',
                    bbox_inches='tight', pad_inches=0.1, dpi=150)
    
    if show:
        plt.show()


if __name__ == "__main__":
    heatmap('roc_auc')
