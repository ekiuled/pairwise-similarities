from similarities.similarity import Similarity
from gensim.models import Word2Vec
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Input, LSTM, Dropout, Bidirectional
from keras.layers.normalization import BatchNormalization
from keras.layers.embeddings import Embedding
from keras.layers.merge import concatenate
from keras.models import Model
import numpy as np


class SiameseSimilarity(Similarity):
    """Siamese neural network similarity."""

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
        self.epochs = 25

    def similarity(self, x, y):
        return self.run_similarity([x, y])

    def run_similarity(self, pairs):
        """Predict similarity for each pair."""

        comments1, comments2, word_counts = self.features(pairs)
        if not hasattr(self, 'model'):
            raise ValueError('running neural network without training.')
        return list(self.model.predict([comments1, comments2, word_counts], verbose=1).ravel())

    def train(self, pairs, labels):
        """Define and train the neural network."""

        # Flatten list of comment pairs
        comments = list(np.ravel(pairs))
        comments = list(map(text_to_word_sequence, comments))
        # Train word2vec embeddings
        word2vec = Word2Vec(comments, min_count=1, size=self.embedding_dimension)
        # Train tokenizer
        self.tokenizer = Tokenizer()
        self.tokenizer.fit_on_texts(comments)
        word_index = self.tokenizer.word_index
        vocab_size = len(word_index) + 1
        # Generate embedding matrix
        self.embedding_matrix = np.zeros((vocab_size, self.embedding_dimension))
        for word, i in word_index.items():
            self.embedding_matrix[i] = word2vec.wv[word]
        del word2vec

        # Define the neural network
        # Word embedding layer
        embedding_layer = Embedding(vocab_size, self.embedding_dimension, weights=[self.embedding_matrix],
                                    input_length=self.max_sequence_length, trainable=False)
        # LSTM encoder
        lstm_layer = Bidirectional(LSTM(self.number_lstm_units, dropout=self.rate_drop_lstm, recurrent_dropout=self.rate_drop_lstm))
        # LSTM encoder layer for the 1st comment
        input1 = Input(shape=(self.max_sequence_length,), dtype='int32')
        embedding1 = embedding_layer(input1)
        lstm1 = lstm_layer(embedding1)
        # LSTM encoder layer for the 2nd comment
        input2 = Input(shape=(self.max_sequence_length,), dtype='int32')
        embedding2 = embedding_layer(input2)
        lstm2 = lstm_layer(embedding2)
        # Word count layer
        input3 = Input(shape=(3,))
        dense3 = Dense(int(self.number_dense_units/2), activation=self.activation_function)(input3)
        # Merge two LSTM layers and the dense word count layer
        merged = concatenate([lstm1, lstm2, dense3])
        # [Normalization + dropout + dense] x2
        merged = BatchNormalization()(merged)
        merged = Dropout(self.rate_drop_dense)(merged)
        merged = Dense(self.number_dense_units, activation=self.activation_function)(merged)
        merged = BatchNormalization()(merged)
        merged = Dropout(self.rate_drop_dense)(merged)
        output = Dense(1, activation='sigmoid')(merged)
        # Initialize the model
        self.model = Model(inputs=[input1, input2, input3], outputs=output)
        self.model.compile(loss='binary_crossentropy', optimizer='nadam', metrics=['acc'])

        # Extract features from pairs
        comments1, comments2, word_counts = self.features(pairs)
        # Train the model
        self.model.fit([comments1, comments2, word_counts], labels, epochs=self.epochs)
        

    def features(self, pairs):
        """Get features from comment pairs: tokenized sequences and word counts."""

        comments1, comments2 = map(list, zip(*pairs))
        comments1 = self.tokenizer.texts_to_sequences(comments1)
        comments2 = self.tokenizer.texts_to_sequences(comments2)
        word_counts = [[len(set(x1)), len(set(x2)), len(set(x1).intersection(x2))]
                       for x1, x2 in zip(comments1, comments2)]
        comments1 = pad_sequences(comments1, self.max_sequence_length)
        comments2 = pad_sequences(comments2, self.max_sequence_length)
        return comments1, comments2, np.array(word_counts)
