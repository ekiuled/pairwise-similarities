from similarities.similarity import Similarity
import difflib
from normalizer import words


class LCSSimilarity(Similarity):
    def similarity(self, x, y):
        x = words(x)
        y = words(y)
        sm = difflib.SequenceMatcher(None, x, y)
        blocks = sm.get_matching_blocks()[:-1]
        matching = 0
        x = list(map(len, x))
        y = list(map(len, y))
        for start, _, length in blocks:
            matching += sum(x[start:start+length])
        total = sum(x) + sum(y)
        return 2 * matching / total
