# Normalization

Normalization is the process of transforming text into a standard format. This involves converting Arabic characters and numbers to Persian equivalants, replacing spaces with ZERO WIDTH NON-JOINER (Half-Space) if needed, and handling special characters. Normalization is an essential step in natural language processing (NLP) as it helps in reducing the complexity of the text and improving the performance of machine learning models, search engines, and text analysis tools.

## Normalizer

The `Normalizer` is a tool used to standardize a given text. This is particularly useful in natural language processing tasks where consistency and uniformity of the text are important. The `Normalizer` can handle various text transformations such as lowercasing, removing punctuation, and handling special characters.

Below is an example of how to use the `Normalizer`:

```python
from shekar.normalizers import Normalizer

text = "ۿدف ما ػمګ بۀ ێڪډيڱڕ أښټ"
normalizer = Normalizer()
normalized_text = normalizer.normalize(text)

print(normalized_text)
```

```output
هدف ما کمک به یکدیگر است
```