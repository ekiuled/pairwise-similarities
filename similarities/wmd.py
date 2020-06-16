from similarities.similarity import Similarity
from keras.preprocessing.text import text_to_word_sequence
from gensim.models import Word2Vec
import numpy as np


class WMDSimilarity(Similarity):
    """Word mover's distance similarity."""

    def __init__(self):
        """Segmentation and normalization are not allowed in WMD similarity."""

        super().__init__()
        self.embedding_dimension = 50
        self.model_cache = 'cache/models/wmd'

    def similarity(self, x, y):
        x = text_to_word_sequence(x)
        y = text_to_word_sequence(y)
        return -self.word2vec.wv.wmdistance(x, y)

    def load(self, cache):
        """Load trained model."""

        self.word2vec = Word2Vec.load(self.model_cache)
        super().load(cache)

    def train(self, pairs, labels, verbose=False, cache=None):
        """Train word2vec embeddings."""

        # Flatten list of comment pairs
        comments = list(np.ravel(pairs))
        comments = list(map(text_to_word_sequence, comments))
        # Train word2vec embeddings
        self.word2vec = Word2Vec(comments, min_count=1, size=self.embedding_dimension)
        # Save
        if cache:
            self.word2vec.save(self.model_cache)
        super().train(pairs, labels, verbose, cache)
