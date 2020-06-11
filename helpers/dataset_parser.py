import re
import csv


def extract(filename):
    """Extract comments and their group tags into two lists."""

    left_br = '<!-- .+ <=< ACCEPT -->'
    right_br = '<!-- ACCEPT >=> .+ -->'
    pattern = re.compile(left_br + '[\w\W]+?' + right_br)
    f = open(filename, 'r')
    result = pattern.findall(f.read())

    comments = [re.sub(left_br, '', re.sub(right_br, '', r)) for r in result]
    groups = [re.sub('<!-- ', '', re.sub(' <=< ACCEPT -->[\w\W]*', '', r))
              for r in result]

    return comments, groups


def generate_pairs(comments, groups):
    """Generate labeled pairs of comments from a list of comments with their group tags."""

    n = len(comments)
    pairs = []

    for i in range(0, n):
        for j in range(i + 1, n):
            pairs.append([comments[i], comments[j], int(groups[i] == groups[j])])

    return pairs


def list_to_file(list, filename):
    """Write a list to a file in csv format."""

    with open(filename, 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in list:
            writer.writerow(item)


def list_from_file(filename):
    """Read a csv into a list."""

    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def dataset_from_file(filename):
    """Make a list of pairs and a list of whether comments in a pair are similar (0 or 1)."""

    pairs = []
    similar = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pairs.append([row[0], row[1]])
            similar.append(int(row[2]))
    return pairs, similar


def cache_similarity_to_file(file_in, file_out, similarity):
    """Apply similarity to all elements of the input dataset and write results and labels to the output file."""

    pairs, y = dataset_from_file(file_in)
    x = similarity.run_similarity(pairs)
    data = zip(x, y)
    list_to_file(data, file_out)


def get_cache_from_file(filename):
    """Read cached similarities and labels into two lists."""

    data = list_from_file(filename)
    scores, labels = list(map(list, zip(*data)))
    return list(map(float, scores)), list(map(int, labels))


def parse(filename, postfix=''):
    """Generate a dataset of labeled comment pairs and write it to a file."""

    comments, groups = extract(filename)
    data = generate_pairs(comments, groups)
    list_to_file(data, 'data_' + postfix + '.csv')
