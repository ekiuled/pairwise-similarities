from similarities.similarity import Similarity
from scipy.spatial.distance import cosine
from sklearn.feature_extraction.text import CountVectorizer


class COSSimilarity(Similarity):
    def similarity(self, x, y):
        e1, e2 = CountVectorizer(token_pattern=r'(?u)\b\w+\b').fit_transform([x, y]).toarray()
        return 1 - cosine(e1, e2)
