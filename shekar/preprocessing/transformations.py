from typing import Iterable
from shekar.base import BaseTextTransformer
import shekar.utils as utils
import re
import emoji
import polars as pl
import html
import string


class PunctuationNormalizer(BaseTextTransformer):
    def __init__(self):
        super().__init__()
        self.punctuation_mappings = [
            (r"[▕❘❙❚▏│]", "|"),
            (r"[ㅡ一—–ー̶]", "-"),
            (r"[▁_̲]", "_"),
            (r"[❔?�؟ʕʔ🏻\x08\x97\x9d]", "؟"),
            (r"[❕！]", "!"),
            (r"[⁉]", "!؟"),
            (r"[‼]", "!!"),
            (r"[℅%]", "٪"),
            (r"[÷]", "/"),
            (r"[×]", "*"),
            (r"[：]", ":"),
            (r"[›]", ">"),
            (r"[‹＜]", "<"),
            (r"[《]", "«"),
            (r"[》]", "»"),
            (r"[•]", "."),
            (r"[٬,]", "،"),
            (r"[;；]", "؛"),
        ]

        self._patterns = self._compile_patterns(self.punctuation_mappings)

    def _function(self, X, y=None):
        return self._map_patterns(X, self._patterns)


class AlphabetNormalizer(BaseTextTransformer):
    """
    Normalizes Arabic characters to Persian characters.
    This class is used to convert Arabic characters to their Persian equivalents.
    """

    def __init__(self):
        super().__init__()
        self.character_mappings = [
            (r"[ﺁﺂ]", "آ"),
            (r"[أٲٵ]", "أ"),
            (r"[ﭐﭑٳﺇﺈإٱ]", "ا"),
            (r"[ؠٮٻڀݐݒݔݕݖﭒﭕﺏﺒ]", "ب"),
            (r"[ﭖﭗﭘﭙﭚﭛﭜﭝ]", "پ"),
            (r"[ٹٺټٿݓﭞﭟﭠﭡﭦﭨﺕﺘ]", "ت"),
            (r"[ٽݑﺙﺚﺛﺜﭢﭤ]", "ث"),
            (r"[ڃڄﭲﭴﭵﭷﺝﺟﺠ]", "ج"),
            (r"[ڇڿﭺݘﭼﮀﮁݯ]", "چ"),
            (r"[ځڂڅݗݮﺡﺤ]", "ح"),
            (r"[ﺥﺦﺧ]", "خ"),
            (r"[ڈډڊڋڍۮݙݚﮂﮈﺩ]", "د"),
            (r"[ڌﱛﺫﺬڎڏڐﮅﮇ]", "ذ"),
            (r"[ڑڒړڔڕږۯݛﮌﺭ]", "ر"),
            (r"[ڗݫﺯﺰ]", "ز"),
            (r"[ڙﮊﮋ]", "ژ"),
            (r"[ښڛﺱﺴ]", "س"),
            (r"[ڜۺﺵﺸݜݭ]", "ش"),
            (r"[ڝڞﺹﺼ]", "ص"),
            (r"[ۻﺽﻀ]", "ض"),
            (r"[ﻁﻃﻄ]", "ط"),
            (r"[ﻅﻆﻈڟ]", "ظ"),
            (r"[ڠݝݞݟﻉﻊﻋ]", "ع"),
            (r"[ۼﻍﻎﻐ]", "غ"),
            (r"[ڡڢڣڤڥڦݠݡﭪﭫﭬﻑﻒﻓ]", "ف"),
            (r"[ٯڧڨﻕﻗ]", "ق"),
            (r"[كػؼڪګڬڭڮݢݣﮎﮐﯓﻙﻛ]", "ک"),
            (r"[ڰڱڲڳڴﮒﮔﮖ]", "گ"),
            (r"[ڵڶڷڸݪﻝﻠ]", "ل"),
            (r"[۾ݥݦﻡﻢﻣ]", "م"),
            (r"[ڹںڻڼڽݧݨݩﮞﻥﻧ]", "ن"),
            (r"[ﯝٷﯗﯘﺅٶ]", "ؤ"),
            (r"[ﯙﯚﯜﯞﯟۄۅۉۊۋۏﯠﻭפ]", "و"),
            (r"[ﮤۂ]", "ۀ"),
            (r"[ھۿہۃەﮦﮧﮨﮩﻩﻫة]", "ه"),
            (r"[ﮰﮱٸۓ]", "ئ"),
            (r"[ﯷﯹ]", "ئی"),
            (r"[ﯻ]", "ئد"),
            (r"[ﯫ]", "ئا"),
            (r"[ﯭ]", "ئه"),
            (r"[ﯰﯵﯳ]", "ئو"),
            (
                r"[ؽؾؿىيۍێېۑےﮮﮯﯤﯥﯦﯧﯼﯽﯾﯿﻯﻱﻳﯨﯩﱝ]",
                "ی",
            ),
        ]

        self._patterns = self._compile_patterns(self.character_mappings)

    def _function(self, X, y=None):
        return self._map_patterns(X, self._patterns)


class ArabicUnicodeNormalizer(BaseTextTransformer):
    """
    Normalizes special Arabic unicode characters to their Persian equivalents.
    """

    def __init__(self):
        super().__init__()
        self.unicode_mappings = [
            ("﷽", "بسم الله الرحمن الرحیم"),
            ("﷼", "ریال"),
            ("(ﷰ|ﷹ)", "صلی"),
            ("ﷲ", "الله"),
            ("ﷳ", "اکبر"),
            ("ﷴ", "محمد"),
            ("ﷵ", "صلعم"),
            ("ﷶ", "رسول"),
            ("ﷷ", "علیه"),
            ("ﷸ", "وسلم"),
            ("ﻵ|ﻶ|ﻷ|ﻸ|ﻹ|ﻺ|ﻻ|ﻼ", "لا"),
        ]

        self._patterns = self._compile_patterns(self.unicode_mappings)

    def _function(self, X, y=None):
        return self._map_patterns(X, self._patterns)


class NumericNormalizer(BaseTextTransformer):
    """
    Normalizes Arabic, English and other unicode number signs to Persian numbers.
    """

    def __init__(self):
        super().__init__()
        self._number_mappings = [
            (r"[0٠𝟢𝟬]", "۰"),
            (r"[1١𝟣𝟭⑴⒈⓵①❶𝟙𝟷ı]", "۱"),
            (r"[2٢𝟤𝟮⑵⒉⓶②❷²𝟐𝟸𝟚ᒿշ]", "۲"),
            (r"[3٣𝟥𝟯⑶⒊⓷③❸³ვ]", "۳"),
            (r"[4٤𝟦𝟰⑷⒋⓸④❹⁴]", "۴"),
            (r"[5٥𝟧𝟱⑸⒌⓹⑤❺⁵]", "۵"),
            (r"[6٦𝟨𝟲⑹⒍⓺⑥❻⁶]", "۶"),
            (r"[7٧𝟩𝟳⑺⒎⓻⑦❼⁷]", "۷"),
            (r"[8٨𝟪𝟴⑻⒏⓼⑧❽⁸۸]", "۸"),
            (r"[9٩𝟫𝟵⑼⒐⓽⑨❾⁹]", "۹"),
            (r"[⑽⒑⓾⑩]", "۱۰"),
            (r"[⑾⒒⑪]", "۱۱"),
            (r"[⑿⒓⑫]", "۱۲"),
            (r"[⒀⒔⑬]", "۱۳"),
            (r"[⒁⒕⑭]", "۱۴"),
            (r"[⒂⒖⑮]", "۱۵"),
            (r"[⒃⒗⑯]", "۱۶"),
            (r"[⒄⒘⑰]", "۱۷"),
            (r"[⒅⒙⑱]", "۱۸"),
            (r"[⒆⒚⑲]", "۱۹"),
            (r"[⒇⒛⑳]", "۲۰"),
        ]
        self._patterns = self._compile_patterns(self._number_mappings)

    def _function(self, X, y=None):
        return self._map_patterns(X, self._patterns)


class PunctuationRemover(BaseTextTransformer):
    """
    Removes all punctuations from the text.
    If keep_persian is True, it will only remove non-Persian punctuations.
    """

    def __init__(self, keep_persian=False):
        super().__init__()

        self._punctuation_mappings = [
            (r"[^\w\s]", ""),
        ]
        if not keep_persian:
            self._punctuation_mappings = [
                (rf"[{utils.punctuations}]+", ""),
            ]

        self._patterns = self._compile_patterns(self._punctuation_mappings)

    def _function(self, text: str) -> str:
        return self._map_patterns(text, self._patterns)


class DiacriticsRemover(BaseTextTransformer):
    """
    Removes Arabic diacritics from the text.
    If diacritics is None, it will remove all Arabic diacritics.
    If diacritics is a string, it will remove only the specified diacritics.
    """

    def __init__(self):
        super().__init__()
        self._diacritic_mappings = [
            (rf"[{utils.diacritics}]", ""),
        ]

        self._patterns = self._compile_patterns(self._diacritic_mappings)

    def _function(self, text: str) -> str:
        return self._map_patterns(text, self._patterns)


class EmojiRemover(BaseTextTransformer):
    """
    Removes emojis from the text.
    """

    def __init__(self):
        super().__init__()

    def _function(self, text: str) -> str:
        return emoji.replace_emoji(text, replace="")


class EmailMasker(BaseTextTransformer):
    """
    Masks email addresses in the text.
    """

    def __init__(self, mask: str = "<EMAIL>"):
        super().__init__()
        self.mask = mask
        self._email_mappings = [
            (r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", self.mask),
        ]
        self._patterns = self._compile_patterns(self._email_mappings)

    def _function(self, text: str) -> str:
        return self._map_patterns(text, self._patterns)


class URLMasker(BaseTextTransformer):
    """
    Masks URLs in the text.
    """

    def __init__(self, mask: str = "<URL>"):
        super().__init__()
        self.mask = mask
        self._url_mappings = [
            (r"(https?://[^\s]+)", self.mask),
        ]
        self._patterns = self._compile_patterns(self._url_mappings)

    def _function(self, text: str) -> str:
        return self._map_patterns(text, self._patterns)


class SpacingStandardizer(BaseTextTransformer):
    """
    Standardizes spacing in the text regarding the offical Persian script standard published by the Iranian Academy of Language and Literature.
    reference: https://apll.ir/
    This class is also used to remove extra spaces, newlines, zero width nonjoiners, and other unicode space characters.
    """

    def __init__(self):
        super().__init__()
        self._spacing_mappings = [
            (r" {2,}", " "),  # remove extra spaces
            (r"\n{3,}", "\n\n"),  # remove extra newlines
            (r"\u200c{2,}", "\u200c"),  # remove extra ZWNJs
            (r"\u200c{1,} ", " "),  # remove ZWNJs before space
            (r" \u200c{1,}", " "),  # remove ZWNJs after space
            (r"\b\u200c*\B", ""),  # remove ZWNJs at the beginning of words
            (r"\B\u200c*\b", ""),  # remove ZWNJs at the end of words
            (
                r"[\u200b\u200d\u200e\u200f\u2066\u2067\u202a\u202b\u202d]",
                "",
            ),  # remove other unicode space characters
        ]

        self._patterns = self._compile_patterns(self._spacing_mappings)

    def _function(self, text: str) -> str:
        # A POS tagger is needed to identify part of speech tags in the text.

        text = re.sub(r"^(بی|می|نمی)( )", r"\1‌", text)  # verb_prefix
        text = re.sub(r"( )(می|نمی)( )", r"\1\2‌ ", text)  # verb_prefix
        text = re.sub(r"([^ ]ه) ی ", r"\1‌ی ", text)

        return self._map_patterns(text, self._patterns).strip()


class StopwordRemover(BaseTextTransformer):
    """
    Removes Persian stopwords from the text.
    """

    def __init__(self, stopwords: Iterable[str] = None):
        super().__init__()
        self.stopwords = stopwords or utils.stopwords

    def _function(self, text: str) -> str:
        words = text.split()
        return " ".join(
            word
            for word in words
            if not self.stopwords.filter(pl.col("word") == word).height > 0
        )


class HTMLTagRemover(BaseTextTransformer):
    """
    Removes HTML tags and entities from the text.
    """

    def __init__(self):
        super().__init__()
        self._html_tag_mappings = [
            (r"<[^>]+>", ""),
        ]

        self._patterns = self._compile_patterns(self._html_tag_mappings)

    def _function(self, text: str) -> str:
        text = html.unescape(text)
        return self._map_patterns(text, self._patterns)


class RedundantCharacterRemover(BaseTextTransformer):
    """
    Removes more than two repeated letters and every keshida from the text.
    """

    def __init__(self):
        super().__init__()
        self._redundant_mappings = [
            (r"[ـ]", ""),  # remove keshida
            (r"([^\s])\1{2,}", r"\1\1"),  # remove more than two repeated letters
        ]

        self._patterns = self._compile_patterns(self._redundant_mappings)

    def _function(self, text: str) -> str:
        return self._map_patterns(text, self._patterns)


class NonPersianRemover(BaseTextTransformer):
    """
    Removes non-Persian letters from the text.
    """

    def __init__(self, keep_english=False, keep_diacritics=False):
        super().__init__()

        self.characters_to_keep = (
            utils.persian_letters
            + utils.spaces
            + utils.persian_digits
            + utils.punctuations
        )

        if keep_diacritics:
            self.characters_to_keep += utils.diacritics

        if keep_english:
            self.characters_to_keep += (
                string.ascii_letters + string.digits + string.punctuation
            )

        self._filter_mappings = [
            (r"[^" + self.characters_to_keep + r"]+", ""),
        ]
        self._patterns = self._compile_patterns(self._filter_mappings)

    def _function(self, text: str) -> str:
        return self._map_patterns(text, self._patterns)
