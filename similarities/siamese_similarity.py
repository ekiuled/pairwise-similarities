from similarities.similarity import Similarity


class SiameseSimilarity(Similarity):
    """Siamese neural network similarity."""

    def __init__(self):
        """Segmentation and normalization are not allowed in Siamese similarity."""

        super().__init__()

    def similarity(self, x, y):
        pass

    def train(self, pairs, labels):
        pass
