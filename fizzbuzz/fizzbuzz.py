#!/usr/bin/env python


def fizzbuzz(param):
    if param % 3 == 0 and param % 5 == 0:
        return "FizzBuzz"
    if param % 3 == 0:
        return "Fizz"
    if param % 5 == 0:
        return "Buzz"
    return param