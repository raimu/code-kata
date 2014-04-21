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
]


def test_roman_to_int():
    for arabic, roman in ARABIC_TO_ROMAN:
        assert int(Roman(roman)) == arabic

