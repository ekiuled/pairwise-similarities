from abc import ABC, abstractmethod
from vectorizer import vectorize, composite_tag
from normalizer import normalize
from scipy.optimize import linprog


class Similarity(ABC):
    def __init__(self, vectorized=False):
        self.vectorized = vectorized

    def run_similarity(self, data):
        """Applies the similarity function to each element of the list."""

        similarities = []

        if self.vectorized:
            for item in data:
                similarities.append(
                    self.vectorized_similarity(item[0], item[1]))
        else:
            for item in data:
                similarities.append(self.similarity(
                    normalize(item[0]), normalize(item[1])))

        return similarities

    def vectorized_similarity(self, x, y):
        """Parses two strings as vectors of JavaDoc tags and calculates their similarity."""

        x = vectorize(x)
        y = vectorize(y)
        result = 0
        length = 0

        for key in {**x, **y}.keys():
            xval = x.get(key, '')
            yval = y.get(key, '')
            if xval and yval:
                if key in ['@param', '@exception', '@throws']:
                    xlist = [normalize(val) for val in composite_tag(xval, key)]
                    ylist = [normalize(val) for val in composite_tag(yval, key)]
                    result += self.composite_similarity(xlist, ylist) * (len(xval) + len(yval))
                else:
                    xval = normalize(xval)
                    yval = normalize(yval)
                    result += self.similarity(xval, yval) * (len(xval) + len(yval))
                length += len(xval) + len(yval)

        return result / length if length else 0

    def composite_similarity(self, x, y):
        """Matches optimally elements of two lists and calculates their similarity."""

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
        """Calculates raw similarity of two strings."""

        pass
