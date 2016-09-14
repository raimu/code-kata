package com.github.raimu.fizzbuzz;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TestFizzBuzz {

    @Test
    public void testFizzbuzzShouldReturnNumberAsDefault() {
        assertEquals("1", FizzBuzz.getFizzBuzz(1));
        assertEquals("4", FizzBuzz.getFizzBuzz(4));
    }

    @Test
    public void testFizzBuzzShouldReturnFizzWhenDivisibleByThree() {
        assertEquals("Fizz", FizzBuzz.getFizzBuzz(3));
        assertEquals("Fizz", FizzBuzz.getFizzBuzz(6));
    }

    @Test
    public void testFizzBuzzShouldReturnBuzzWhenDivisibleByFive() {
        assertEquals("Buzz", FizzBuzz.getFizzBuzz(5));
        assertEquals("Buzz", FizzBuzz.getFizzBuzz(10));
    }

    @Test
    public void testFizzBuzzShouldReturnFizzBuzzWhenDivisibleByThreeAndFive() {
        assertEquals("FizzBuzz", FizzBuzz.getFizzBuzz(15));
    }
}
