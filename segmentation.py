from collections import defaultdict
from scipy.optimize import linprog


def segment(s):
    """Parses input into a dictionary of JavaDoc tags.

    Parameters
    ----------
    s : str

    Returns
    -------
    dict
        Dictionary of JavaDoc tags: keys - tag names, values - vectors of tag instances.
    """

    tags = defaultdict(list)
    tag = ''

    for line in s.splitlines():
        if line and line[0] == '@':
            if len(line.split(maxsplit=1)) == 2:
                tag, line = line.split(maxsplit=1)
            else:
                tag = line.split(maxsplit=1)[0]
                line = ''
            tags[tag].append(line)
        elif not tags:
            tags[tag] = [line]
        else:
            tags[tag][-1] += ' ' + line

    return tags
