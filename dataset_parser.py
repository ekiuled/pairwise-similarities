import re
import csv


def extract(filename):
    """Extracts comments and their group names into two lists."""

    left_br = '<!-- .+ <=< ACCEPT -->'
    right_br = '<!-- ACCEPT >=> .+ -->'
    pattern = re.compile(left_br + '[\w\W]+?' + right_br)
    f = open(filename, 'r')
    result = pattern.findall(f.read())

    cropped = [re.sub(left_br, '', re.sub(right_br, '', r)) for r in result]
    group = [re.sub('<!-- ', '', re.sub(' <=< ACCEPT -->[\w\W]*', '', r))
             for r in result]

    return cropped, group


def parse_to_list(cropped, group):
    """Generates pairs from lists of comments and their group names."""

    n = len(cropped)
    pairs = []

    for i in range(0, n):
        for j in range(i + 1, n):
            pairs.append([cropped[i], cropped[j], int(group[i] == group[j])])

    return pairs


def list_to_file(list, filename='data.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in list:
            writer.writerow(item)


def list_from_file(filename):
    """Makes a list out of a csv file."""

    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def dataset_from_file(filename):
    """Makes a list of pairs and a list of whether comments in a pair are similar."""

    pairs = []
    similar = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pairs.append([row[0], row[1]])
            similar.append(row[2])
    return pairs, similar


def cache_similarity_to_file(file_in, file_out, similarity):
    pairs, y = dataset_from_file(file_in)

    len1 = []
    len2 = []
    for pair in pairs:
        l1, l2 = len(pair[0]), len(pair[1])
        len1.append(min(l1, l2))
        len2.append(max(l1, l2))

    x = similarity.run_similarity(pairs)
    data = zip(x, len1, len2, y)
    list_to_file(data, file_out)


def get_similarity_and_groups_from_file(filename):
    data = list_from_file(filename)
    return list(map(lambda x: [x[0], x[3]], data))


def parse(filename, postfix=''):
    cropped, group = extract(filename)
    data = parse_to_list(cropped, group)
    list_to_file(data, 'data_' + postfix + '.csv')


if __name__ == '__main__':
    pass
    # parse('/home/cthfvrl/diploma/Datasets/O.23.SLF4J/SLF4J__7c2f6cd1.2019-12-XX_dluciv_dkoznov_marked.txt', 'slf4j_full')
    # parse('/home/cthfvrl/diploma/Datasets/O.21.JUnit4/junit4__9e98a85.dkoznov_dluciv_2019.12_marked_2_pairs.txt', 'junit4_full')
    # parse('/home/cthfvrl/diploma/Datasets/O.22.Mockito/mockito__196ff979.2019-12-XX_dluciv_dkoznov_marked.txt', 'mockito_full')
    # parse('/home/cthfvrl/diploma/Datasets/O.24.GSON/GSON_2b08c88c.dluciv_marked.txt', 'gson_full')
