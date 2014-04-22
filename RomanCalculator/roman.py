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
        self.number = number

    def __int__(self):
        result = 0
        number = self.number
        for arabic, roman in self.arabic_roman_map:
            while number.startswith(roman):
                result += arabic
                number = number[len(roman):]
        return result