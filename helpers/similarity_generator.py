from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.lev_similarity import LEVSimilarity
from similarities.lsh_similarity import LSHSimilarity
from helpers import dataset_parser as parser


def map(func):
    """Apply a function to all combinations of algorithms and pipelines.
    
    Parameters
    ----------
    func : function(model, model_name)
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
            func(model, title + suffix)


def map_cache(func):
    """Apply a function to all combinations of algorithms and pipelines.
    Values are read from cache.
    
    Parameters
    ----------
    func : function(model_name, pairs, labels)
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
            pairs, groups = parser.get_cache_from_file(
                'cache/' + title + suffix)
            func(title + ' ' + suffix, pairs, groups)


def map_time_cache(func):
    """Apply a function to the cached execution time list for all combinations of algorithms and pipelines.
    
    Parameters
    ----------
    func : function(time_list, model_name)
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
            func(times, title + suffix)
