from similarities.similarity import Similarity
from keras.preprocessing.text import text_to_word_sequence
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from scipy.spatial.distance import cosine
import numpy as np


class D2VKSimilarity(Similarity):
    """Doc2vec similarityusing this: https://www.kaggle.com/isofew/code-comment-pairs
    Kaggle dataset for wor2vec training."""

    def __init__(self):
        """Segmentation and normalization are not allowed in doc2vec similarity."""

        super().__init__()
        self.embedding_dimension = 50
        self.epochs = 20
        self.steps = 100
        self.model_cache = 'cache/models/d2vk'

    def similarity(self, x, y):
        x_vec = self.doc2vec.infer_vector(text_to_word_sequence(x), steps=self.steps)
        y_vec = self.doc2vec.infer_vector(text_to_word_sequence(y), steps=self.steps)
        return 1 - cosine(x_vec, y_vec)

    def load(self, cache):
        """Load trained model."""

        self.doc2vec = Doc2Vec.load(self.model_cache)
        super().load(cache)

    def train(self, pairs, labels, verbose=False, cache=None):
        """Train word2vec embeddings."""

        self.doc2vec = Doc2Vec.load(self.model_cache)
        super().train(pairs, labels, verbose, cache)
