from similarities.similarity import Similarity
from keras.preprocessing.text import text_to_word_sequence
from gensim.models import Word2Vec
import numpy as np
import pandas as pd


class WMDKSimilarity(Similarity):
    """Word mover's distance similarity using this: https://www.kaggle.com/isofew/code-comment-pairs
    Kaggle dataset for wor2vec training."""

    def __init__(self):
        """Segmentation and normalization are not allowed in WMD similarity."""

        super().__init__()
        self.embedding_dimension = 50
        self.model_cache = 'cache/models/w2v'

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

        # # Train
        # reader = pd.read_csv('data/kaggle/code.csv', chunksize=10**5, usecols=['doc'], lineterminator='\n')
        # empty = True
        # for chunk in reader:
        #     comments = list(map(text_to_word_sequence, chunk['doc']))
        #     if empty:
        #         self.word2vec = Word2Vec(comments, min_count=1, size=self.embedding_dimension)
        #         empty = False
        #     else:
        #         self.word2vec.build_vocab(comments, update=True)
        #         self.word2vec.train(comments, total_examples=len(comments), epochs=self.word2vec.epochs)

        # # Save
        # if cache:
        #     self.word2vec.save(self.model_cache)
        self.word2vec = Word2Vec.load(self.model_cache)
        super().train(pairs, labels, verbose, cache)
