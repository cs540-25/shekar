import pytest
from shekar.embeddings import Embedding
import requests


def test_model_urls():
    for model_name, url in Embedding.available_models.items():
        response = requests.head(url)
        assert response.status_code == 200, (
            f"Model {model_name} URL {url} is not reachable"
        )


def test_load_model():
    embedding = Embedding()
    assert embedding.model.doesnt_match("خیار گوجه سنگ کاهو".split()) == "سنگ"
