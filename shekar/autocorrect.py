from collections import Counter
from shekar.tokenizers import WordTokenizer


class AutoCorrect:
    _letters = "آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"

    def __init__(self, words: Counter):
        self.tokenizer = WordTokenizer()
        self.n_words = sum(words.values())
        self.words = {word: freq / self.n_words for word, freq in words.items()}

    @classmethod
    def generate_1edits(cls, word):
        deletes = [word[:i] + word[i + 1 :] for i in range(len(word))]
        inserts = [
            word[:i] + c + word[i:] for i in range(len(word) + 1) for c in cls._letters
        ]
        replaces = [
            word[:i] + c + word[i + 1 :] for i in range(len(word)) for c in cls._letters
        ]
        transposes = [
            word[:i] + word[i + 1] + word[i] + word[i + 2 :]
            for i in range(len(word) - 1)
        ]
        return set(deletes + inserts + replaces + transposes)

    @classmethod
    def generate_n_edits(cls, word, n=1):
        edits_1 = cls.generate_1edits(word)
        if n == 1:
            return edits_1
        else:
            edits_n = set()
            for edit in edits_1:
                edits_n |= cls.generate_n_edits(edit, n=n - 1)
            return edits_n

    def correct(self, word, n=5):
        suggestions = []
        if word in self.words:
            suggestions.append((word, self.words[word]))

        suggestions += sorted(
            [
                (w, self.words[w])
                for w in self.generate_n_edits(word, n=1)
                if w in self.words
            ],
            key=lambda x: x[1],
            reverse=True,
        )
        suggestions += sorted(
            [
                (w, self.words[w])
                for w in self.generate_n_edits(word, n=2)
                if w in self.words
            ],
            key=lambda x: x[1],
            reverse=True,
        )

        seen = set()
        unique_suggestions = []
        for suggestion in suggestions:
            if suggestion[0] not in seen:
                unique_suggestions.append(suggestion[0])
            seen.add(suggestion[0])

        return unique_suggestions[:n]

    def correct_text(self, text):
        tokens = self.tokenizer.tokenize(text)
        return " ".join(self.correct(token)[0] for token in tokens)
