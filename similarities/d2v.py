from similarities.similarity import Similarity
from keras.preprocessing.text import text_to_word_sequence
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from scipy.spatial.distance import cosine
import numpy as np


class D2VSimilarity(Similarity):
    """Doc2vec similarity."""

    def __init__(self):
        """Segmentation and normalization are not allowed in doc2vec similarity."""

        super().__init__()
        self.embedding_dimension = 50
        self.epochs = 20
        self.steps = 100
        self.model_cache = 'cache/models/d2v'

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

        comments = list(np.ravel(pairs))
        comments = list(map(text_to_word_sequence, comments))
        documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(comments)]
        self.doc2vec = Doc2Vec(documents, vector_size=self.embedding_dimension, min_count=1, epochs=self.epochs)
        if cache:
            self.doc2vec.save(self.model_cache)
        super().train(pairs, labels, verbose, cache)
