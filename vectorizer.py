from collections import defaultdict


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
