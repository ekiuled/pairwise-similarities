# pairwise-similarities

Code collection for comparative analysis of text similarity algorithms for detecting near duplicates in JavaDoc software documentation.

## Folder structure

- `similarity`: similarity algorithms.   
- `helpers`: functions for dataset generation and parsing, caching and similarity algorithm exhaustion.   
- `datasets`: source project files and generated datasets.   
- `cache`: cached similarities for the test dataset.   
- `pipeline`: segmentation and normalization functions.   
- `metrics`: functions for algorithm evaluation.   
- `stats`: evaluation results.   
- `visualization`: functions for result visualization.   

## Similarity algorithms

- Cosine distance (via term frequency vectors)
- Longest common subsequence (token-wise)
- Levenshtein distance
- Locality sensitive hashing
- Siamese neural network (via wor2vec embeddings and LSTM)
- Word mover's distance (via word2vec)

## Usage

Run one of the functions from the `metrics` folder, providing it with necessary datasets.