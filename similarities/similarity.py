from abc import ABC, abstractmethod
from pipeline.segmentation import segment
from pipeline.normalizer import normalize
from scipy.optimize import linprog


class Similarity(ABC):
    """Similarity base class. 
    
    Override `similarity(x, y)` method for customization.
    Call `run_similarity` on a list of pairs to get a list of similarities.
    """

    def __init__(self, segmentation=False, normalization=None):
        self.segmentation = segmentation
        if normalization == 'full':
            self.normalize = lambda s: normalize(s, True)
        elif normalization == 'partial':
            self.normalize = lambda s: normalize(s)
        else:
            self.normalize = lambda s: s

    def run_similarity(self, pairs):
        """Apply the similarity function to each element of the list."""

        similarities = []

        if self.segmentation:
            for pair in pairs:
                similarities.append(
                    self.vectorized_similarity(pair[0], pair[1]))
        else:
            for pair in pairs:
                similarities.append(self.similarity(
                    self.normalize(pair[0]), self.normalize(pair[1])))

        return similarities

    def vectorized_similarity(self, x, y):
        """Parse two strings as vectors of JavaDoc tags and calculate their similarity."""

        x = segment(x)
        y = segment(y)
        result = 0
        length = 0

        for key in {**x, **y}.keys():
            xval = x.get(key, None)
            yval = y.get(key, None)
            if xval and yval:
                xval = [self.normalize(val) for val in xval]
                yval = [self.normalize(val) for val in yval]
                len_sum = sum(list(map(len, xval))) + sum(list(map(len, yval)))
                if len(xval) > 1 or len(yval) > 1:
                    result += self.composite_similarity(xval, yval) * len_sum
                else:
                    result += self.similarity(xval[0], yval[0]) * len_sum
                length += len_sum

        return result / length if length else 0

    def composite_similarity(self, x, y):
        """Match optimally elements of two lists and calculate their similarity."""

        s = [-self.similarity(p, q) for p in x for q in y]
        n = len(x)
        m = len(y)
        A = [[0]*(m*i) + [1]*m + [0]*(m*(n-i-1)) for i in range(n)]
        for i in range(m):
            A.append([0]*(n*m))
            for j in range(n):
                A[n + i][i + j*m] = 1
        res = linprog(s, A_ub=A, b_ub=[1]*(n+m), options=dict(lstsq=True))
        return -res.get('fun') / min(n, m)

    @abstractmethod
    def similarity(self, x, y):
        """Calculate raw similarity of two strings."""

        pass
