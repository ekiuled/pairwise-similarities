from similarities.similarity import Similarity
import difflib


class LCSSimilarity(Similarity):
    def similarity(self, x, y):
        sm = difflib.SequenceMatcher()
        sm.set_seqs(x, y)
        return sm.ratio()
