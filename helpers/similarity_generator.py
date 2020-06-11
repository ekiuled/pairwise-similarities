from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.lev_similarity import LEVSimilarity
from similarities.lsh_similarity import LSHSimilarity
from helpers import dataset_parser as parser


def all_similarities():
    """Yield all combinations of algorithms and pipelines.
    
    Yields
    ------
    tuple
        Title and similarity.
    """

    models = [[] for _ in range(4)]
    suffixes = []
    for segmentation in [False, True]:
        for normalization in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(segmentation, normalization))
            models[1].append(COSSimilarity(segmentation, normalization))
            models[2].append(LEVSimilarity(segmentation, normalization))
            models[3].append(LSHSimilarity(segmentation, normalization))
            suffix = str(segmentation) + str(normalization)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'LEV', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            yield title + suffix, model


def all_similarities_cached():
    """Yield cached values for all combinations of algorithms and pipelines.
    
    Yields
    ------
    tuple
        Similarity title, similarity scores and labels.
    """

    models = [[] for _ in range(4)]
    suffixes = []
    for segmentation in [False, True]:
        for normalization in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(segmentation, normalization))
            models[1].append(COSSimilarity(segmentation, normalization))
            models[2].append(LEVSimilarity(segmentation, normalization))
            models[3].append(LSHSimilarity(segmentation, normalization))
            suffix = str(segmentation) + str(normalization)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'LEV', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            scores, labels = parser.get_cache_from_file(
                'cache/' + title + suffix)
            yield title + ' ' + suffix, scores, labels


def similarity_time_cached():
    """Yield cached execution time for all combinations of algorithms and pipelines.
    
    Yields
    ------
    tuple
        Similarity title and time list.
    """

    models = [[] for _ in range(4)]
    suffixes = []
    for segmentation in [False, True]:
        for normalization in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(segmentation, normalization))
            models[1].append(COSSimilarity(segmentation, normalization))
            models[2].append(LEVSimilarity(segmentation, normalization))
            models[3].append(LSHSimilarity(segmentation, normalization))
            suffix = str(segmentation) + str(normalization)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'LEV', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            times = [float(line)
                     for line in open('cache/time/' + title + suffix, 'r')]
            yield title + suffix, times
