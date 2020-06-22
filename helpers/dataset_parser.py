import re
import pandas as pd
import json


def comment(string):
    """Extract comment body."""

    open_accept = '<!-- .+ <=< ACCEPT -->'
    close_accept = '<!-- ACCEPT >=> .+ -->'
    meta_pattern = '<!-- META [\w\W]+? -->'
    comment = re.sub(close_accept, '', re.sub(open_accept, '',  re.sub(meta_pattern, '', string)))
    return re.sub('[ ]+', ' ', comment)


def group_tag(string):
    """Extract group tag."""

    left_br = '><!-- '
    right_br = ' <=< ACCEPT -->'
    accept = re.search(left_br + '.+' + right_br, string)
    if not accept:
        return ''
    return re.sub(left_br, '', re.sub(right_br, '', accept.group(0)))


def object_name(meta):
    """Extract object name from metadata."""

    json_string = re.sub(' -->', '', (re.sub('<!-- META ', '', meta)))
    try:
        signature = json.loads(json_string)['entitySignature']
    except:
        return ''
    if '(' not in signature:
        return signature
    return re.search('[^\s]+?\(', signature).group(0)[:-1]


def extract(filename):
    """Extract all comments, object names, metadata and group tags."""

    f = open(filename, 'r')
    pattern = re.compile('(<!--[^\n\r]+(\n[ ]+[^\n\r]+)*)')
    instances = [match[0] for match in pattern.findall(f.read())]

    meta_pattern = '<!-- META [\w\W]+? -->'
    meta = [re.search(meta_pattern, inst).group(0) for inst in instances]
    object_names = [object_name(m) for m in meta]

    nonempty_name_idx = [i for i in range(len(object_names)) if object_names[i]]
    instances = [instances[i] for i in nonempty_name_idx]
    meta = [meta[i] for i in nonempty_name_idx]
    object_names = [object_names[i] for i in nonempty_name_idx]

    comments = [comment(inst) for inst in instances]
    group_tags = [group_tag(inst) for inst in instances]

    return comments, object_names, meta, group_tags


def generate_pairs(comments, object_names, meta, group_tags, skip_untagged=True):
    """Generate a dataframe of labeled comment pairs."""

    n = len(comments)
    data = []

    for i in range(n):
        for j in range(i + 1, n):
            if group_tags[i] and group_tags[j]:
                label = int(group_tags[i] == group_tags[j])
            elif skip_untagged:
                continue
            else:
                label = -1
            data.append([comments[i], comments[j],
                         object_names[i], object_names[j],
                         meta[i], meta[j],
                         label])

    return pd.DataFrame(data, columns=['comment1', 'comment2', 'name1', 'name2', 'meta1', 'meta2', 'label'])


def parse(file_in, file_out, skip_untagged=True):
    """Generate a dataset of unique labeled comment pairs and save it in a file."""

    comments, object_names, meta, group_tags = extract(file_in)
    df = generate_pairs(comments, object_names, meta, group_tags, skip_untagged)
    df.drop_duplicates(inplace=True)
    df.to_csv(file_out)
