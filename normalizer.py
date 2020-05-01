from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from string import punctuation
from collections import defaultdict

table = str.maketrans('', '', punctuation)


def normalize(s, remove_stopwords=False):
    tag_map = defaultdict(lambda: wordnet.NOUN)
    tag_map['J'] = wordnet.ADJ
    tag_map['V'] = wordnet.VERB
    tag_map['R'] = wordnet.ADV

    tokens = word_tokenize(s)

    lemmatizer = WordNetLemmatizer()
    filtered = [lemmatizer.lemmatize(token.lower(), tag_map[tag[0]])
                for token, tag in pos_tag(tokens) if not token in punctuation]

    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        filtered = [w for w in tokens if not w in stop_words]

    return ' '.join(filtered)


def words(s):
    return s.translate(table).split()
