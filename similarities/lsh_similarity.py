from similarities.similarity import Similarity
from lsh import minhash, cache


class LSHSimilarity(Similarity):
    def similarity(self, x, y):
        n = 100
        bands = 50
        hasher = minhash.MinHasher(seeds=n, char_ngram=3)
        lshcache = cache.Cache(num_bands=bands, hasher=hasher)
        lshcache.add_fingerprint(hasher.fingerprint(x.encode('utf8')), 1)
        lshcache.add_fingerprint(hasher.fingerprint(y.encode('utf8')), 2)

        collisions = 0
        for bin in lshcache.bins:
            for _, bucket in bin.items():
                collisions += len(bucket) - 1

        return collisions / bands

    def minhash_similarity(self, x, y):
        hasher = minhash.MinHasher(seeds=100, char_ngram=3)
        x = set(hasher.fingerprint(x.encode('utf8')))
        y = set(hasher.fingerprint(y.encode('utf8')))
        return len(x & y) / len(x | y)
