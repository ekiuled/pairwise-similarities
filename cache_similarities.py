from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.levenshtein_similarity import LevenshteinSimilarity
from similarities.lsh_similarity import LSHSimilarity
from logistic_regression import Model
import dataset_parser as parser


def cache(filename):
    models = [[] for _ in range(4)]
    names = []
    for vectorized in [False, True]:
        for normalized in [None, 'partial', 'full']:
            models[0].append(LCSSimilarity(vectorized, normalized))
            models[1].append(COSSimilarity(vectorized, normalized))
            models[2].append(LevenshteinSimilarity(vectorized, normalized))
            models[3].append(LSHSimilarity(vectorized, normalized))
            suffix = str(vectorized) + str(normalized)
            names.append(suffix)

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, name in zip(algorithm, names):
            parser.cache_similarity_to_file(filename, 'cache/' + title + name, model)


if __name__ == "__main__":
    cache('dataset.csv')
