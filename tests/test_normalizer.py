import pytest
from shekar.normalizer import Normalizer


@pytest.fixture
def normalizer():
    return Normalizer()


def test_normalize_numbers(normalizer):
    input_text = "٠١٢٣٤٥٦٧٨٩ ⒕34"
    expected_output = "۰۱۲۳۴۵۶۷۸۹ ۱۴۳۴"
    assert normalizer.normalize(input_text) == expected_output


def test_unify_characters(normalizer):
    input_text = "نشان‌دهندة"
    expected_output = "نشان‌دهنده"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "دربارۀ ما"
    expected_output = "دربارۀ ما"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "نامۀ فرهنگستان"
    expected_output = "نامۀ فرهنگستان"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "رئالیسم رئیس لئیم"
    expected_output = "رئالیسم رئیس لئیم"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "رأس متلألئ مأخذ"
    expected_output = "رأس متلألئ مأخذ"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "مؤلف مؤمن مؤسسه"
    expected_output = "مؤلف مؤمن مؤسسه"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "جزء"
    expected_output = "جزء"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "سایة"
    expected_output = "سایه"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "ۿدف ما ػمګ بۃ ێڪډيڱڕ إښټ"
    expected_output = "هدف ما کمک به یکدیگر است"
    print(normalizer.normalize(input_text))
    print(expected_output)
    assert normalizer.normalize(input_text) == expected_output

    input_text = "روزی باغ ســـــــــــــــــــبــــــــــــــــــز بود"
    expected_output = "روزی باغ سبز بود"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "کارتون"
    expected_output = "کارتون"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "همه با هم در برابر پلیدی و ستم خواهیم ایستاد"
    expected_output = "همه با هم در برابر پلیدی و ستم خواهیم ایستاد"
    assert normalizer.normalize(input_text) == expected_output


def test_unify_punctuations(normalizer):
    input_text = "؟?،٬!%:«»؛"
    expected_output = "؟؟،،!٪:«»؛"
    assert normalizer.normalize(input_text) == expected_output


def test_remove_emojis(normalizer):
    input_text = "😊🇮🇷سلام گلای تو خونه!🎉🎉🎊🎈"
    expected_output = "سلام گلای تو خونه!"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "🌹 باز هم مرغ سحر🐔 بر سر منبر گل "
    expected_output = "باز هم مرغ سحر بر سر منبر گل"
    print(normalizer.normalize(input_text))
    print(expected_output)
    assert normalizer.normalize(input_text) == expected_output


def test_remove_diacritics(normalizer):
    input_text = "مَنْ"
    expected_output = "من"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "کُجا نِشانِ قَدَم ناتَمام خواهَد ماند؟"
    expected_output = "کجا نشان قدم ناتمام خواهد ماند؟"
    assert normalizer.normalize(input_text) == expected_output


def test_unify_arabic_unicode(normalizer):
    input_text = "﷽"
    expected_output = "بسم الله الرحمن الرحیم"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "پنجاه هزار ﷼"
    expected_output = "پنجاه هزار ریال"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "ﷲ اعلم "
    expected_output = "الله اعلم"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "ﷲ ﷳ"
    expected_output = "الله اکبر"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "ﷴ"
    expected_output = "محمد"
    assert normalizer.normalize(input_text) == expected_output


# def test_remove_punctuations(normalizer):
#     input_text = "$@^<</من:<, ()).^%!?میروم"
#     expected_output = "من میروم"
#     assert normalizer.normalize(input_text) == expected_output


def test_correct_spacings(normalizer):
    """Tests normalization with a Persian sentence."""
    input_text = "   این یک جمله   نمونه   است. "
    expected_output = "این یک جمله نمونه است."
    assert normalizer.normalize(input_text) == expected_output

    input_text = "اینجا کجاست؟تو میدونی؟نمیدونم!"
    expected_output = "اینجا کجاست؟تو میدونی؟نمیدونم!"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "ناصر گفت:«من می‌روم.»"
    expected_output = "ناصر گفت:«من می‌روم.»"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "با کی داری حرف می زنی؟"
    expected_output = "با کی داری حرف می زنی؟"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "من می‌روم.تو نمی‌آیی؟"
    expected_output = "من می‌روم.تو نمی‌آیی؟"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "به نکته ریزی اشاره کردی!"
    expected_output = "به نکته ریزی اشاره کردی!"
    assert normalizer.normalize(input_text) == expected_output


def test_remove_extra_spaces(normalizer):
    input_text = "این  یک  آزمون  است"
    expected_output = "این یک آزمون است"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "این  یک\n\n\nآزمون  است"
    expected_output = "این یک\n\nآزمون است"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "این\u200cیک\u200cآزمون\u200cاست"
    expected_output = "این\u200cیک\u200cآزمون\u200cاست"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "این\u200c یک\u200c آزمون\u200c است"
    expected_output = "این یک آزمون است"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "این  یک  آزمون  است  "
    expected_output = "این یک آزمون است"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "این  یک  آزمون  است\n\n\n\n"
    expected_output = "این یک آزمون است"
    assert normalizer.normalize(input_text) == expected_output


def test_mask_email(normalizer):
    input_text = "ایمیل من: she.kar@shekar.panir.io"
    expected_output = "ایمیل من:"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "ایمیل من: she+kar@she-kar.io"
    expected_output = "ایمیل من:"
    assert normalizer.normalize(input_text) == expected_output


def test_mask_url(normalizer):
    input_text = "لینک: https://shekar.parsi-shekar.com"
    expected_output = "لینک:"
    assert normalizer.normalize(input_text) == expected_output

    input_text = "لینک: http://shekar2qand.com/id=2"
    expected_output = "لینک:"
    assert normalizer.normalize(input_text) == expected_output


def test_normalize(normalizer):
    input_text = "ناصر گفت:«من می‌روم.» \u200c 🎉🎉🎊🎈she+kar@she-kar.io"
    expected_output = "ناصر گفت:«من می‌روم.»"
    assert normalizer.normalize(input_text) == expected_output
