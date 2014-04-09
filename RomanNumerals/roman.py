#!/usr/bin/env python


class RomanNumeralsError(Exception):
    pass


def to_roman(number):
    if int(number) != number:
        raise RomanNumeralsError("only integer allowed")
    if number <= 0 or number >= 5000:
        raise RomanNumeralsError("number out of allowed range (1-4999)")
    result = ""
    for roman, arabic in [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
                          ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
                          ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]:
        while number >= arabic:
            result += roman
            number -= arabic
    return result