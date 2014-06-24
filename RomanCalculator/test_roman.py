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


def test_lowercase():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert str(Roman(roman.lower())) == roman


def test_roman_int_to_int():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert int(Roman(arabic)) == arabic


def test_compare_eq():
    assert Roman("IV") == Roman(4)


def test_compare_ne():
    assert Roman("III") != Roman(4)


def test_compare_lt():
    assert Roman("III") < 4


def test_compare_gt():
    assert Roman("IV") > 3


def test_compare_le():
    assert Roman("I") <= 1


def test_compare_ge():
    assert Roman("I") >= 1


def test_plus():
    assert Roman("I") + 1 == Roman("II")


def test_minus():
    assert Roman("IV") - 1 == Roman("III")


def test_multiplication():
    assert Roman("II") * 2 == Roman("IV")


def test_division():
    assert Roman("IV") / 2 == Roman("II")


def test_modulo():
    assert Roman("III") % 2 == Roman("I")


def test_pow():
    assert Roman("2") ** 2 == Roman("IV")