#!/usr/bin/env python


def fizzbuzz(param):
    return (not param % 3) * 'Fizz' + (not param % 5) * 'Buzz' or param
