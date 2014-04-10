#!/usr/bin/env python


class RomanNumeralsError(Exception):
    pass


ROMAN_ARABIC_MAP = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                    ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                    ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]


def to_roman(number):
    try:
        if int(number) != number:
            raise RomanNumeralsError("only integer allowed")
    except ValueError:
        raise RomanNumeralsError("only integer allowed")
    if number <= 0 or number >= 5000:
        raise RomanNumeralsError("number out of allowed range (1-4999)")
    result = ""
    for roman, arabic in ROMAN_ARABIC_MAP:
        while number >= arabic:
            result += roman
            number -= arabic
    return result


def from_roman(roman_number):
    result = 0
    while roman_number:
        any_match = False
        for roman, arabic in ROMAN_ARABIC_MAP:
            if roman_number.startswith(roman):
                roman_number = roman_number[len(roman):]
                result += arabic
                any_match = True
        if not any_match:
            break
    return result