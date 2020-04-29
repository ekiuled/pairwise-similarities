from similarities.similarity import Similarity
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


class COSSimilarity(Similarity):
    def similarity(self, x, y):
        vectorizer = CountVectorizer()
        try:
            embeddings = vectorizer.fit_transform([x, y])
        except ValueError:
            # Strings consisted of stopwords or numbers only,
            # usually happens in the @since tag
            return x == y
        return cosine_similarity(embeddings[0:1], embeddings[1:2])[0, 0]
