import unittest

from domain.roman_numerals.test_roman_numerals import translate_numeral


class TestRomanNumerals(unittest.TestCase):
    def test_translation_from_one_to_nine(self):
        self.assertEqual("II", translate_numeral("2"))
        self.assertEqual("V", translate_numeral("5"))
        self.assertEqual("X", translate_numeral("10"))

    def test_translation_from_eleven_to_forty_nine(self):
        self.assertEqual("XI", translate_numeral("11"))
        self.assertEqual("XV", translate_numeral("15"))
        self.assertEqual("XVII", translate_numeral("17"))
        self.assertEqual("XIX", translate_numeral("19"))
        self.assertEqual("XX", translate_numeral("20"))
        self.assertEqual("XXV", translate_numeral("25"))
        self.assertEqual("XXIX", translate_numeral("29"))
        self.assertEqual("XXXV", translate_numeral("35"))
        self.assertEqual("XL", translate_numeral("40"))
        self.assertEqual("XLIX", translate_numeral("49"))

    def test_translation_from_fifty_to_ninty_nine(self):
        self.assertEqual("L", translate_numeral("50"))
        self.assertEqual("LV", translate_numeral("55"))
        self.assertEqual("LIX", translate_numeral("59"))
        self.assertEqual("LXXV", translate_numeral("75"))
        self.assertEqual("XCIX", translate_numeral("99"))

    def test_translation_from_one_hundred_to_nine_hundred_ninty_nine(self):
        self.assertEqual("C", translate_numeral("100"))
        self.assertEqual("CCXLVI", translate_numeral("246"))
        self.assertEqual("DCCLXXXIX", translate_numeral("789"))
        self.assertEqual("CMXCIX", translate_numeral("999"))

    def test_translation_from_one_thousand_to_three_thousand_nine_hundred_ninty_nine(self):
        self.assertEqual("M", translate_numeral("1000"))
        self.assertEqual("MMCDXXI", translate_numeral("2421"))
        self.assertEqual("MMMCMXCIX", translate_numeral("3999"))


if __name__ == '__main__':
    unittest.main()
