from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
from similarities.lsh_similarity import LSHSimilarity
import dataset_parser as parser


def map(func):
    models = [[] for _ in range(4)]
    suffixes = []
    for segmentation in [False, True]:
        for normalization in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(segmentation, normalization))
            models[1].append(COSSimilarity(segmentation, normalization))
            models[2].append(LevenshteinSimilarity(segmentation, normalization))
            models[3].append(LSHSimilarity(segmentation, normalization))
            suffix = str(segmentation) + str(normalization)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            func(model, title + suffix)


def map_cache(func):
    models = [[] for _ in range(4)]
    suffixes = []
    for segmentation in [False, True]:
        for normalization in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(segmentation, normalization))
            models[1].append(COSSimilarity(segmentation, normalization))
            models[2].append(LevenshteinSimilarity(segmentation, normalization))
            models[3].append(LSHSimilarity(segmentation, normalization))
            suffix = str(segmentation) + str(normalization)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            pairs, groups = parser.get_cache_from_file(
                'cache/' + title + suffix)
            func(title + ' ' + suffix, pairs, groups)


def map_time_cache(func):
    models = [[] for _ in range(4)]
    suffixes = []
    for segmentation in [False, True]:
        for normalization in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(segmentation, normalization))
            models[1].append(COSSimilarity(segmentation, normalization))
            models[2].append(LevenshteinSimilarity(segmentation, normalization))
            models[3].append(LSHSimilarity(segmentation, normalization))
            suffix = str(segmentation) + str(normalization)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            times = [float(line)
                     for line in open('cache/time/' + title + suffix + '.txt', 'r')]
            func(times, title + suffix)
