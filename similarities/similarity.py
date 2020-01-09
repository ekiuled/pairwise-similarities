from abc import ABC, abstractmethod


class Similarity(ABC):
    def run_similarity(self, data):
        """Applies similarity function to each element in the dataset."""

        similarities = []

        for item in data:
            similarities.append(self.similarity(item[0], item[1]))

        return similarities


    @abstractmethod
    def similarity(self, x, y):
        """Takes two strings as arguments and returns their similarity."""

        pass
