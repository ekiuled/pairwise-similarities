from similarities.similarity import Similarity
from scipy.spatial.distance import cosine
from normalizer import words


class COSSimilarity(Similarity):
    """Cosine TF-based similarity."""

    def similarity(self, x, y):
        d = {}
        wx = words(x)
        wy = words(y)
        for w in wx:
            d[w] = [0, 0]
        for w in wy:
            d[w] = [0, 0]
        for w in wx:
            d[w][0] += 1
        for w in wy:
            d[w][1] += 1

        e1 = [v[0] for v in d.values()]
        e2 = [v[1] for v in d.values()]

        return 1 - cosine(e1, e2)
