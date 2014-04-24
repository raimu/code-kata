#!/usr/bin/env python
from RomanCalculator.roman import Roman


ARABIC_TO_ROMAN = [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (14, "XIV"),
    (42, "XLII"),
    (80, "LXXX"),
    (94, "XCIV"),
    (100, "C"),
    (444, "CDXLIV"),
    (553, "DLIII"),
    (911, "CMXI"),
    (2014, "MMXIV"),
]


def test_roman_string_to_int():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert int(Roman(roman)) == arabic


def test_roman_int_to_string():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert str(Roman(arabic)) == roman


def test_roman_string_to_string():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert str(Roman(roman)) == roman


def test_roman_int_to_int():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert int(Roman(arabic)) == arabic


def test_compare_eq():
    assert Roman("IV") == Roman(4)


def test_compare_ne():
    assert Roman("III") != Roman(4)