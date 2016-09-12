#!/usr/bin/env python
from unittest import TestCase
from mock import MagicMock, patch
from fizzbuzz.fizzbuzz import fizzbuzz
from fizzbuzz.fizzbuzz import main


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


def test_main():
    mock = MagicMock()
    with patch('builtins.print', new=mock):
        main()
    mock.assert_any_call(1)
    mock.assert_any_call("Fizz")
    mock.assert_any_call("Buzz")
    mock.assert_any_call("FizzBuzz")
    mock.assert_any_call(16)
