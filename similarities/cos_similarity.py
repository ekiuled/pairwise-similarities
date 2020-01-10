from similarities.similarity import Similarity
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class COSSimilarity(Similarity):
    def similarity(self, x, y):
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([x, y])
        return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0, 0]
