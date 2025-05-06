# Word Embeddings

Word embeddings are vector representations of words in a continuous vector space. They capture semantic relationships between words, allowing similar words to have closer vector representations. This is essential in natural language processing (NLP) as it enhances machine learning models' ability to understand text, perform clustering, and analyze semantic similarity.

## Embedding Class

The `Embedding` class provides a simple interface for loading and using pre-trained word embeddings. It supports FastText word vectors and allows retrieving word representations and finding similar words.

### Installation

```python
from shekar.embeddings import Embedding
```

### Available Models

The following pre-trained models are available for use:

- `fasttext-d300-w5-cbow-naab`: Trained on the Naab corpus with 300-dimensional word vectors.
- `fasttext-d100-w10-cbow-blogs`: Trained on Persian blog texts with 100-dimensional word vectors.

### Initialization

To initialize the `Embedding` class with a specific model:

```python
embedding = Embedding(model_name="fasttext-d100-w10-cbow-blogs")
```

### Usage

#### 1. Get Word Vector
Retrieve the vector representation of a word:

```python
vector = embedding["کتاب"]
print(vector)  # Output: Numpy array of word vector
```

#### 2. Find Similar Words
Find the top-N most similar words based on cosine similarity:

```python
similar_words = embedding.most_similar("کتاب", topn=5)
print(similar_words)
```

## Best Practices

1. Use pre-trained embeddings for better generalization in NLP tasks.
2. Initialize and reuse a single `Embedding` instance to avoid redundant loading.
3. Ensure the model is correctly downloaded and extracted before use.
4. Handle out-of-vocabulary words gracefully when retrieving word vectors.
5. Choose the appropriate model based on the dataset and application.

## Common Issues and Solutions

1. **Model not found**: Ensure the model name is correct and available in the `available_models` dictionary.
2. **Download failure**: Check internet connection and retry downloading.
3. **Word not in vocabulary**: Use subword information if supported or consider using a larger dataset.
4. **Large memory usage**: Consider using lower-dimensional embeddings if memory is a constraint.
5. **Encoding issues**: Ensure input text is properly encoded in UTF-8 before processing.

By leveraging the `Embedding` class, users can efficiently integrate word embeddings into their Persian NLP applications, enhancing their text analysis and machine learning tasks.