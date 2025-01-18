import pytest
from shekar.normalizer import Normalizer


@pytest.fixture
def normalizer():
    return Normalizer()


def test_normalize_numbers(normalizer):
    input_text = "٠١٢٣٤٥٦٧٨٩"
    expected_output = "۰۱۲۳۴۵۶۷۸۹"
    assert normalizer.normalize(input_text) == expected_output


def test_unify_characters(normalizer):
    input_text = "نشان‌دهندة"
    expected_output = "نشان‌دهنده"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "سایة"
    expected_output = "سایه"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "ۿدف ما ػمګ بۀ ێڪډيڱڕ أښټ"
    expected_output = "هدف ما کمک به یکدیگر است"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "کارتون"
    expected_output = "کارتون"
    assert normalizer.normalize(input_text) == expected_output

    # correct examples
    input_text = "همه با هم در برابر پلیدی و ستم خواهیم ایستاد"
    expected_output = "همه با هم در برابر پلیدی و ستم خواهیم ایستاد"
    assert normalizer.normalize(input_text) == expected_output


def test_normalize_marks(normalizer):
    input_text = "؟?،٬!%:«»؛"
    expected_output = "؟؟،،!٪:«»؛"
    assert normalizer.normalize(input_text) == expected_output
