import re


class Normalizer:
    def __init__(
        self,
        unify_numbers: bool = True,
        unify_marks: bool = True,
        unify_by_resemblance: bool = False,
    ):
        self._unify_numbers = unify_numbers
        self._unify_marks = unify_marks
        self._unify_by_resemblance = unify_by_resemblance

        self._character_mappings = [
            (r"[ۃةہەۀۂھۿ]", "ه"),
            (r"[ڵڶڷڸ]", "ل"),
            (r"[ڰ-ڴ]", "گ"),
            (r"[ىيؿؾؽێۍۑېےۓؠ]", "ی"),
            (r"[ۋۄۅۆۇۈۊۉۏٷؤٶ]", "و"),
            (r"[ػؼكڪګڬڭڮكﻙ]", "ک"),
            (r"[إأٱٲٳٵ]", "ا"),
            (r"[ڹںڻڼ]", "ن"),
            (r"[ړڔڕږڒۯ]", "ر"),
            (r"[ٺټ]", "ت"),
            (r"[ٻ]", "ب"),
            (r"[ۺ]", "ش"),
            (r"[ۼ]", "غ"),
            (r"[ۻ]", "ض"),
            (r"[ڝ]", "ص"),
            (r"[ڛښ]", "س"),
            (r"[ڇڿ]", "چ"),
            (r"[ډڊڍ]", "د"),
            (r"[ڣ]", "ف"),
        ]

        self._persian_characters = " آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی"
        self._persian_numbers = "۰۱۲۳۴۵۶۷۸۹"
        self._allowed_marks_punct = "٪،؟.!:«»؛"
        self._half_space = "\u200c"

        self._resemblance_based_mappings = [
            (r"[ڃڄ]", "چ"),
            (r"[ځڂ]", "خ"),
            (r"[ڗڙۋ]", "ژ"),
            (r"[ڒۯ]", "ز"),
            (r"[ٽٿٹڽ]", "ث"),
            (r"[ڜ]", "ش"),
            (r"[ڠ]", "غ"),
            (r"[ڥ]", "پ"),
            (r"[ڤڦڨ]", "ق"),
            (r"[ڞ]", "ض"),
            (r"[ڋڌڈڎڏڐ]", "ذ"),
            (r"[؋]", "ف"),
            (r"[ڟ]", "ظ"),
        ]

        self._marks_mappings = [(r"[?⸮]", "؟"), (r"[,٬]", "،"), (r"[%]", "٪")]

        self._numbers_translation_map = str.maketrans(
            "٠١٢٣٤٥٦٧٨٩0123456789", self._persian_numbers * 2
        )

        self._all_mappings = []
        self._all_mappings.extend(self._character_mappings)

        if unify_marks:
            self._all_mappings.extend(self._marks_mappings)
        if unify_by_resemblance:
            self._all_mappings.extend(self._resemblance_based_mappings)

    def normalize(self, text):
        for pattern, replacement in self._all_mappings:
            text = re.sub(pattern, replacement, text)
        if self._unify_numbers:
            text = text.translate(self._numbers_translation_map)
        return self.remove_non_persian(text)

    def unify_numbers(self, text):
        text = text.translate(self._numbers_translation_map)
        return text

    def unify_marks(self, text):
        for pattern, replacement in self._marks_mappings:
            text = re.sub(pattern, replacement, text)
        return text

    def unify_characters(self, text):
        for pattern, replacement in self._character_mappings:
            text = re.sub(pattern, replacement, text)
        return text

    def unify_by_resemblance(self, text):
        for pattern, replacement in self._resemblance_based_mappings:
            text = re.sub(pattern, replacement, text)
        return text

    def remove_non_persian(self, text):
        allowed_characters = (
            self._persian_characters
            + self._persian_numbers
            + self._allowed_marks_punct
            + self._half_space
        )
        pattern = f"[^{re.escape(allowed_characters)}]"
        return re.sub(pattern, "", text)
