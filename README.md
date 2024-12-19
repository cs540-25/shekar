
![Banner](assets/banner.png)

<p align="center">
    <em>Simplifying Persian NLP for Everyone</em>
</p>

<p align="center">
 <a href="https://img.shields.io/github/actions/workflow/status/amirivojdan/shekar/test.yml" target="_blank">
 <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/amirivojdan/shekar/test.yml?color=00A693">
</a>
<a href="https://pypi.org/project/shekar" target="_blank">
    <img src="https://img.shields.io/pypi/v/shekar?color=00A693" alt="Package version">
</a>

<a href="https://pypi.org/project/shekar" target="_blank">
    <img src="https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Famirivojdan%2Fshekar%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&color=00A693" alt="Supported Python versions">
</a>
</p>

## Installation

To install the package, you can use `pip`. Run the following command:

```bash
pip install shekar
```


## Usage

Here is a simple example of how to use the `shekar` package:

```python
from shekar.utils import is_informal
from shekar.preprocessing import unify_characters

# Sample text
text = "ۿدف ما ػمګ بۀ ێڪډيڱڕ أښټ"

# Perform text processing
processed_text = unify_characters(text)

print(processed_text)
```

```output
هدف ما کمک به یکدیگر است
```
 

 
