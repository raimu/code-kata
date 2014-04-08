#!/usr/bin/env python


def fizzbuzz(param):
    return (not param % 3) * 'Fizz' + (not param % 5) * 'Buzz' or param


def main():
    for i in range(1, 100):
        print(fizzbuzz(i))


if __name__ == "__main__":
    main()