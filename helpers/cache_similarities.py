from similarities.lcs import LCSSimilarity
from similarities.cos import COSSimilarity
from similarities.lev import LEVSimilarity
from similarities.lsh import LSHSimilarity
from logistic_regression import Model
from helpers import dataset_parser as parser


def cache(filename):
    """Cache all possible combinations of algorithms and pipelines applied to the input file into the cache folder."""

    models = [[] for _ in range(4)]
    names = []
    for segmentation in [False, True]:
        for normalization in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(segmentation, normalization))
            models[1].append(COSSimilarity(segmentation, normalization))
            models[2].append(LEVSimilarity(segmentation, normalization))
            models[3].append(LSHSimilarity(segmentation, normalization))
            suffix = str(segmentation) + str(normalization)
            names.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'LEV', 'LSH']):
        for model, name in zip(algorithm, names):
            parser.cache_similarity_to_file(filename, 'cache/' + title + name, model)
