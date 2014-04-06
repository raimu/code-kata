#!/usr/bin/env python
from unittest import TestCase
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):

    def test_number(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(4), 4)

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(18), "Fizz")
