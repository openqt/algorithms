#!/usr/bin/env python
# coding=utf-8
"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""
from __future__ import print_function


def sum_square(n):
    """sum of the squares of numbers

    :param n: number
    :return: um of the squares
    """
    return sum(i**2 for i in range(1, n+1))


def square_sum(n):
    """square of the sum of numbers

    :param n: number
    :return: square of the sum
    """
    return sum(range(1, n+1))**2


if __name__ == '__main__':
    print(square_sum(100) - sum_square(100))  # 25164150
