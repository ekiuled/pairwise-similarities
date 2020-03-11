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

    composite_tags = ['@param', '@exception', '@throws']
    tags = defaultdict(str)
    tag = ''

    for line in s.splitlines():
        if line and line[0] == '@':
            tag, line = line.split(maxsplit=1)
            if tag in composite_tags:
                line = tag + ' ' + line
        tags[tag] += line + '\n'

    # Remove the excess newline at the end
    tags = {tag: val[:-1] for tag, val in tags.items()}

    # Replace plain strings with lists of values for composite tags
    for tag in composite_tags:
        if tag in tags.keys():
            tags[tag] = composite_tag(tags[tag], tag)

    return tags


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
