from similarity import Similarity
from Levenshtein import ratio


class LevenshteinSimilarity(Similarity):
    def similarity(self, x, y):
        return ratio(x, y)
