#!/usr/bin/python
from RomanNumerals.roman import to_roman, RomanNumeralsError, from_roman
import pytest


ARABIC_TO_ROMAN = [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (12, "XII"),
    (18, "XVIII"),
    (23, "XXIII"),
    (80, "LXXX"),
    (91, "XCI"),
    (411, "CDXI"),
    (555, "DLV"),
    (920, "CMXX"),
    (1999, "MCMXCIX"),
    (3300, "MMMCCC"),
    (4999, "MMMMCMXCIX"),
]


def test_to_roman():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert to_roman(arabic) == roman


def test_to_roman_with_zero():
    with pytest.raises(RomanNumeralsError):
        to_roman(0)


def test_to_roman_to_large():
    with pytest.raises(RomanNumeralsError):
        to_roman(5000)


def test_to_roman_with_float():
    with pytest.raises(RomanNumeralsError):
        to_roman(0.5)


def test_to_roman_with_string():
    with pytest.raises(RomanNumeralsError):
        to_roman("Hello")


def test_from_roman():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert from_roman(roman) == arabic


def test_from_roman_with_invalid_number():
    with pytest.raises(RomanNumeralsError):
        from_roman("ABC")