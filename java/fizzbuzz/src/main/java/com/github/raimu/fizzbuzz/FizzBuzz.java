package com.github.raimu.fizzbuzz;

public class FizzBuzz {
    public static String getFizzBuzz(int number) {
        StringBuilder result = new StringBuilder();
        if (number % 3 == 0) {
            result.append("Fizz");
        }
        if (number % 5 == 0) {
            result.append("Buzz");
        }

        return result.length() == 0 ? Integer.toString(number) : result.toString();
    }
}
