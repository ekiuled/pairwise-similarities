import re
import csv
import itertools
import random


def comment(string):
    """Extract a comment from a single tagged string."""

    left_br = '<!-- .+ <=< ACCEPT -->'
    right_br = '<!-- ACCEPT >=> .+ -->'
    return re.sub(left_br, '', re.sub(right_br, '', string))


def group(string):
    """Extract a group tag from a single string."""

    return re.sub('<!-- ', '', re.sub(' <=< ACCEPT -->[\w\W]*', '', string))


def extract(filename, all=False):
    """Extract all comments, group tags if available and respective object signatures as three lists."""

    f = open(filename, 'r')
    pattern = re.compile('[\w\W]+?\n----------------------\n\n')
    instances = pattern.findall(f.read())

    result = [i.split('\n', 1) for i in instances]
    result = list(filter(lambda x: x[0] != '# Package  /**', result))

    all_signatures, strings = map(list, zip(*result))
    strings = [re.sub('----------------------', '', s).strip('\n') for s in strings]

    comments = []
    groups = []
    signatures = []
    for i in range(len(strings)):
        s = strings[i]
        if '<=< ACCEPT -->' in s:
            comments.append(comment(s))
            groups.append(group(s))
            signatures.append(all_signatures[i])
        elif all:
            comments.append(s)
            groups.append('')
            signatures.append(all_signatures[i])

    return comments, groups, signatures


def generate_pairs(comments, groups):
    """Generate labeled pairs of comments from a list of comments with their group tags."""

    n = len(comments)
    pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            if groups[i] and groups[j]:
                pairs.append([comments[i], comments[j], int(groups[i] == groups[j])])
            else:
                pairs.append([comments[i], comments[j], -1])

    return pairs


def generate_pairs_with_signatures(comments, groups, signatures):
    """Generate labeled pairs of comments and their signatures from a list of comments with their group tags."""

    n = len(comments)
    pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            if groups[i] and groups[j]:
                pairs.append([comments[i], comments[j], int(groups[i] == groups[j]), signatures[i], signatures[j]])
            else:
                pairs.append([comments[i], comments[j], -1, signatures[i], signatures[j]])

    return pairs


def generate_triplets(comments, groups):
    """Generate comment triplets from a list of comments with their group tags."""

    n = len(comments)
    triplets = []

    for i in range(n):
        positive = []
        negative = []
        for j in range(i + 1, n):
            if groups[i] == groups[j]:
                positive.append(comments[j])
            else:
                negative.append(comments[j])
        if negative:
            for p in positive:
                triplets.append([comments[i], p, random.choice(negative)])

    return triplets


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


def parse(file_in, file_out='_data.csv'):
    """Generate a dataset of unique labeled comment pairs and write it to a file."""

    comments, groups, signatures = extract(file_in)
    data = generate_pairs_with_signatures(comments, groups, signatures)
    data.sort()
    data = list(d for d, _ in itertools.groupby(data))
    list_to_file(data, file_out)


def parse_full(file_in, file_out='_data.csv'):
    """Generate a dataset of unique typed comment pairs with labels when available and write it to a file."""

    comments, groups, signatures = extract(file_in, True)
    data = generate_pairs_with_signatures(comments, groups, signatures)
    data.sort()
    data = list(d for d, _ in itertools.groupby(data))
    list_to_file(data, file_out)


def parse_triplets(file_in, file_out='_data.csv'):
    """Generate a dataset of unique comment triplets and write it to a file."""

    comments, groups, _ = extract(file_in)
    data = generate_triplets(comments, groups)
    data.sort()
    data = list(d for d, _ in itertools.groupby(data))
    list_to_file(data, file_out)
