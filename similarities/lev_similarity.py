from similarities.similarity import Similarity
import difflib


class LEVSimilarity(Similarity):
    """Levenshtein distance similarity."""

    def similarity(self, x, y):
        sm = difflib.SequenceMatcher(None, x, y)
        matching = sum([size for _, _, size in sm.get_matching_blocks()])
        total = max(len(x), len(y))
        return matching / total
