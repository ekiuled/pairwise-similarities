from collections import defaultdict
from scipy.optimize import linprog


def vectorize(s):
    """Parses input into a vector of JavaDoc tags.

    Parameters
    ----------
    s : str

    Returns
    -------
    dict
        Dictionary of JavaDoc tags: keys - tag names, values - tag contents.
    """

    tags = defaultdict(str)
    tag = ''

    for line in s.splitlines():
        if line and line[0] == '@':
            tag = line.split(maxsplit=1)[0]
        tags[tag] += line + '\n'

    return {tag: val[:-1] for tag, val in tags.items()}


def composite_tag(source, tag):
    """Parses a composite tag into a list of items. 

    Parameters
    ----------
    source : str
        String containing several tag instances.
    tag : str
        The tag to parse.

    Returns
    -------
    list
        List of tag contents.
    """

    vals = []
    s = ''
    for line in source.splitlines():
        if line.startswith(tag):
            if s:
                vals.append(s)
            s = line.split(maxsplit=1)[1]
        else:
            s += ' ' + line.strip()
    if s:
        vals.append(s)
    return vals
