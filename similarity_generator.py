from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
from similarities.lsh_similarity import LSHSimilarity
import dataset_parser as parser


def map(func):
    models = [[] for _ in range(4)]
    suffixes = []
    for vectorized in [False, True]:
        for normalized in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(vectorized, normalized))
            models[1].append(COSSimilarity(vectorized, normalized))
            models[2].append(LevenshteinSimilarity(vectorized, normalized))
            models[3].append(LSHSimilarity(vectorized, normalized))
            suffix = str(vectorized) + str(normalized)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            func(model, title + ' ' + suffix)


def map_cache(func):
    models = [[] for _ in range(4)]
    suffixes = []
    for vectorized in [False, True]:
        for normalized in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(vectorized, normalized))
            models[1].append(COSSimilarity(vectorized, normalized))
            models[2].append(LevenshteinSimilarity(vectorized, normalized))
            models[3].append(LSHSimilarity(vectorized, normalized))
            suffix = str(vectorized) + str(normalized)
            suffixes.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, suffix in zip(algorithm, suffixes):
            pairs, groups = parser.get_cache_from_file(
                'cache/' + title + suffix)
            func(title + ' ' + suffix, pairs, groups)
