from .base import BaseTransformer


class Pipeline(BaseTransformer):
    def __init__(self, steps: list[tuple[str, BaseTransformer]]):
        self.steps = steps

    def fit(self, X, y=None):
        for name, step in self.steps:
            X = step.fit(X, y)
        return self

    def transform(self, X):
        for name, step in self.steps:
            X = step.transform(X)
        return X

    def fit_transform(self, X, y=None):
        if isinstance(X, str):
            for name, step in self.steps:
                X = step.fit_transform(X, y)
            return X
        elif isinstance(X, list):

            def generator():  # to avoid making the outer function a generator
                for text in X:
                    for name, step in self.steps:
                        text = step.fit_transform(text, y)
                    yield text

            return generator()

        else:
            raise ValueError("Input must be a string or a list of strings.")

    def __call__(self, X):
        return self.fit_transform(X)
