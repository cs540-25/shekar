from typing import Iterable
from shekar import Pipeline
from shekar.preprocessing import (
    PunctuationNormalizer,
    AlphabetNormalizer,
    NumericNormalizer,
    SpacingStandardizer,
    EmojiRemover,
    EmailMasker,
    URLMasker,
    DiacriticsRemover,
    NonPersianRemover,
    HTMLTagRemover,
    RedundantCharacterRemover,
    ArabicUnicodeNormalizer,
)


class Normalizer:
    def __init__(self, pipline: Pipeline = None):
        if pipline is not None:
            self._pipeline = pipline
        else:
            self._pipeline = Pipeline(
                steps=[
                    ("AlphaNumericUnifier", AlphabetNormalizer()),
                    ("ArabicUnicodeNormalizer", ArabicUnicodeNormalizer()),
                    ("NumericNormalizer", NumericNormalizer()),
                    ("PunctuationUnifier", PunctuationNormalizer()),
                    ("EmailMasker", EmailMasker(mask="")),
                    ("URLMasker", URLMasker(mask="")),
                    ("EmojiRemover", EmojiRemover()),
                    ("HTMLTagRemover", HTMLTagRemover()),
                    ("DiacriticsRemover", DiacriticsRemover()),
                    ("RedundantCharacterRemover", RedundantCharacterRemover()),
                    ("NonPersianRemover", NonPersianRemover()),
                    ("SpacingStandardizer", SpacingStandardizer()),
                ]
            )

    def normalize(self, text: Iterable[str] | str):
        return self._pipeline(text)
