#!/usr/bin/env python
from unittest import TestCase
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):

    def test_number(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(4), 4)

    def test_fizz(self):
        """test divisibility by 3"""
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(18), "Fizz")

    def test_buzz(self):
        """test divisibility by 5"""
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_fizzbuzz(self):
        """test divisibility by 3 and 5"""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_not_integer(self):
        self.assertRaises(TypeError, fizzbuzz, "a")
