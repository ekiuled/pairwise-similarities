from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from string import punctuation, whitespace
from collections import defaultdict
import re

delimiter_pattern = '|'.join(map(re.escape, punctuation + whitespace))


def normalize(s, remove_stopwords=False):
    """Lemmatize and remove punctuation and stopwords (optional)."""

    tag_map = defaultdict(lambda: wordnet.NOUN)
    tag_map['J'] = wordnet.ADJ
    tag_map['V'] = wordnet.VERB
    tag_map['R'] = wordnet.ADV

    tokens = words(s)

    lemmatizer = WordNetLemmatizer()
    filtered = [lemmatizer.lemmatize(token.lower(), tag_map[tag[0]])
                for token, tag in pos_tag(tokens)]

    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        filtered = [w for w in tokens if not w in stop_words]

    return ' '.join(filtered)


def words(s):
    """Split a string into words (fast)."""

    return [token.lower() for token in re.split(delimiter_pattern, s) if token]
