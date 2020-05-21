from similarities.lcs_similarity import LCSSimilarity
from similarities.cos_similarity import COSSimilarity
from similarities.lev_similarity import LEVSimilarity
from similarities.lsh_similarity import LSHSimilarity
from logistic_regression import Model
import dataset_parser as parser


def cache(filename):
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

    for algorithm, title in zip(models, ['LCS', 'COS', 'Levenshtein', 'LSH']):
        for model, name in zip(algorithm, names):
            parser.cache_similarity_to_file(filename, 'cache/' + title + name, model)


if __name__ == "__main__":
    cache('dataset.csv')
