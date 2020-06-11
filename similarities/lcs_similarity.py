from similarities.similarity import Similarity
import difflib
from normalizer import words


class LCSSimilarity(Similarity):
    """Longest common subsequence token-based similarity."""

    def similarity(self, x, y):
        x = words(x)
        y = words(y)
        sm = difflib.SequenceMatcher(None, x, y)
        matching = sum([size for _, _, size in sm.get_matching_blocks()])
        total = len(x) + len(y)
        return 2 * matching / total
