from similarities.similarity import Similarity
from datasketch import MinHash, MinHashLSH
from normalizer import words


class LSHSimilarity(Similarity):
    """Locality sensitive hashing similarity."""

    def similarity(self, x, y):
        n = 100
        bands = 50
        m1 = MinHash(num_perm=n)
        m2 = MinHash(num_perm=n)
        for d in self.trigrams(words(x)):
            m1.update(d.encode('utf8'))
        for d in self.trigrams(words(y)):
            m2.update(d.encode('utf8'))
        lsh = MinHashLSH(params=(bands, n // bands), num_perm=n)
        lsh.insert('m1', m1)
        lsh.insert('m2', m2)
        return len(list(filter(lambda x: len(x) == 1, lsh.get_counts()))) / bands

    def trigrams(self, x):
        for i in range(len(x) - 2):
            yield x[i] + ' ' + x[i+1] + ' ' + x[i+2]
