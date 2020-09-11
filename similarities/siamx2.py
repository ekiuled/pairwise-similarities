from similarities.similarity import Similarity
from gensim.models import Word2Vec
from keras.preprocessing.text import Tokenizer, text_to_word_sequence, tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.callbacks import EarlyStopping
from keras.layers import Dense, Input, LSTM, Dropout, Bidirectional
from keras.layers.normalization import BatchNormalization
from keras.layers.embeddings import Embedding
from keras.layers.merge import concatenate
from keras.models import Model, load_model
import json
import numpy as np
import difflib
import pandas as pd


class SiameseX2Similarity(Similarity):
    """Siamese neural network similarity with extra feature."""

    def __init__(self):
        """Segmentation and normalization are not allowed in Siamese similarity."""

        super().__init__()
        self.max_sequence_length = 10
        self.embedding_dimension = 50
        self.number_lstm_units = 50
        self.number_dense_units = 50
        self.rate_drop_lstm = 0.17
        self.rate_drop_dense = 0.25
        self.activation_function = 'relu'
        self.epochs = 20
        self.model_cache = 'cache/models/siamx2'
        self.tokenizer_cache = 'cache/models/tokenizerx'

    def similarity(self, x, y):
        return self.run_similarity([x, y])

    def run_similarity(self, df):
        """Predict similarity for each pair."""

        comments1, comments2, word_counts, name_similarities = self.features(df)
        return np.array(list(self.model.predict([comments1, comments2, word_counts, name_similarities]).ravel()))

    def load(self, cache):
        """Load trained model."""

        self.model = load_model(self.model_cache)
        with open(self.tokenizer_cache) as f:
            self.tokenizer = tokenizer_from_json(json.load(f))
        super().load(cache)

    def train(self, df, verbose=False, cache=None):
        """Train the neural network."""

        labels = df['label'].to_numpy()
        self.model = load_model(self.model_cache)
        super().train(df, labels, verbose, cache)

    def features(self, df):
        """Get features from comment pairs: tokenized sequences, word counts, name similarities."""

        comments1 = df['comment1'].to_numpy()
        comments2 = df['comment2'].to_numpy()
        comments1 = self.tokenizer.texts_to_sequences(comments1)
        comments2 = self.tokenizer.texts_to_sequences(comments2)
        word_counts = [[len(set(x1)), len(set(x2)), len(set(x1).intersection(x2))]
                       for x1, x2 in zip(comments1, comments2)]
        comments1 = pad_sequences(comments1, self.max_sequence_length)
        comments2 = pad_sequences(comments2, self.max_sequence_length)

        names = df[['name1', 'name2']].to_numpy()

        return comments1, comments2, np.array(word_counts), self.get_name_similarities(names)

    def get_name_similarities(self, name_pairs):
        """Get char LCS similarity for each name pair."""

        return np.array([difflib.SequenceMatcher(None, n1, n2).ratio() for n1, n2 in name_pairs])
