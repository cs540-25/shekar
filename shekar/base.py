from abc import ABC, abstractmethod
from typing import Iterable, List
import regex as re


class BaseTransformer(ABC):
    @abstractmethod
    def transform(self, X):
        pass

    @abstractmethod
    def fit(self, X, y=None):
        pass

    @abstractmethod
    def fit_transform(self, X, y=None):
        pass

    def __call__(self, *args, **kwds):
        return self.fit_transform(*args, **kwds)


class BaseTextTransformer(BaseTransformer):
    @abstractmethod
    def _function(self, X: str, y=None) -> str:
        pass

    def transform(self, X: Iterable[str] | str) -> Iterable[str] | str:
        if isinstance(X, str):
            return self._function(X)
        elif isinstance(X, Iterable):
            return (self._function(x) for x in X)
        else:
            raise ValueError("Input must be a string or a Iterable of strings.")

    def fit(self, X: Iterable[str] | str, y=None):
        return self

    def fit_transform(self, X: Iterable[str] | str, y=None):
        return self.transform(X)

    @classmethod
    def _compile_patterns(
        cls, mappings: Iterable[tuple[str, str]]
    ) -> List[tuple[re.Pattern, str]]:
        compiled_patterns = [
            (re.compile(pattern), replacement) for pattern, replacement in mappings
        ]
        return compiled_patterns

    @classmethod
    def _map_patterns(
        cls, text: str, patterns: Iterable[tuple[re.Pattern, str]]
    ) -> str:
        for pattern, replacement in patterns:
            text = pattern.sub(replacement, text)
        return text
