import pandas as pd
from random import sample


def randomized_filter(file_in, file_out):
    """Sample a subset of the negative class from the input dataset of a size 
    of the positive class and write both classes to the output file."""

    df = pd.read_csv(file_in, index_col=0)
    df_neg = df[df['label'] == 0]
    df_pos = df[df['label'] == 1]

    size = len(df_pos.index)
    df_neg = df_neg.sample(size, random_state=42)
    df_filtered = pd.concat([df_pos, df_neg], ignore_index=True)
    df_filtered.to_csv(file_out)


def print_statistics(filename):
    """Print dataset and class sizes."""

    df = pd.read_csv(filename, index_col=0)
    print('Filename:', filename)
    print('Dataset size:', len(df.index))
    print('Class sizes:')
    print(df['label'].value_counts())


def concatenate_datasets(filenames, file_out):
    dfs = []
    for f in filenames:
        dfs.append(pd.read_csv(f, index_col=0))
    df = pd.concat(dfs, ignore_index=True)
    df.to_csv(file_out)
