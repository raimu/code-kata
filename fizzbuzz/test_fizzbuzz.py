#!/usr/bin/env python
from unittest import TestCase
from fizzbuzz.fizzbuzz import fizzbuzz


class TestFizzBuzz(TestCase):

    def test_number(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(4), 4)
