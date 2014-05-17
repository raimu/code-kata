#!/usr/bin/env python


class Roman(object):

    arabic_roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    def __init__(self, number):
        try:
            self._number = int(number)
        except ValueError:
            self._number = self._to_int(number.upper())

    def __int__(self):
        return self._number

    def __str__(self):
        return self._to_string(self._number)

    def __eq__(self, other):
        return self._number == int(other)

    def __lt__(self, other):
        return self._number < int(other)

    def __le__(self, other):
        return self._number <= int(other)

    def __gt__(self, other):
        return self._number > int(other)

    def __ge__(self, other):
        return self._number >= int(other)

    def __add__(self, other):
        return Roman(self._number + int(other))

    def __sub__(self, other):
        return Roman(self._number - int(other))

    def __mul__(self, other):
        return Roman(self._number * int(other))

    def __truediv__(self, other):
        return Roman(self._number / int(other))

    def _to_int(self, roman_number):
        result = 0
        for arabic, roman in self.arabic_roman_map:
            while roman_number.startswith(roman):
                result += arabic
                roman_number = roman_number[len(roman):]
        return result

    def _to_string(self, number):
        result = ""
        for arabic, roman in self.arabic_roman_map:
            while number >= arabic:
                result += roman
                number -= arabic
        return result