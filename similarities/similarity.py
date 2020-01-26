from abc import ABC, abstractmethod
from vectorizer import vectorize
from normalizer import normalize


class Similarity(ABC):
    def __init__(self, vectorized=False):
        self.vectorized = vectorized

    def run_similarity(self, data):
        """Applies similarity function to each element in the dataset."""

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
        """Takes two strings as arguments, parses them as vectors of JavaDoc tags and calculates their similarity."""

        x = vectorize(x)
        y = vectorize(y)
        result = 0
        length = 0

        for key in {**x, **y}.keys():
            xval = x.get(key, '')
            yval = y.get(key, '')
            if key in x and key in y:
                result += self.similarity(normalize(xval),
                                          normalize(yval)) * (len(xval) + len(yval))
            length += len(xval) + len(yval)

        return result / length

    @abstractmethod
    def similarity(self, x, y):
        """Takes two strings as arguments and returns their similarity."""

        pass
