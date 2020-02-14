from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from string import punctuation
from collections import defaultdict


def normalize(s):
    #return s
    tag_map = defaultdict(lambda: wordnet.NOUN)
    tag_map['J'] = wordnet.ADJ
    tag_map['V'] = wordnet.VERB
    tag_map['R'] = wordnet.ADV

    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(s)

    lemmatizer = WordNetLemmatizer()
    filtered = [lemmatizer.lemmatize(token.lower(), tag_map[tag[0]]) for token, tag in pos_tag(tokens) if not token in punctuation]
    
    #filtered = [w for w in tokens if not w in stop_words]
    return ' '.join(filtered)


s = 'Asserts that two longs are equal. If they are not, an\n\
AssertionError is thrown.\n\
\n\
\n\
@param expected expected long value.\n\
@param actual actual long value'
