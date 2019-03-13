#!/usr/bin/env python
# coding=utf-8
"""
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""
from __future__ import print_function


def sum_digit_by(n, func):
    """sum digits of a number with function

    :param n:
    :param func:
    :return:
    """
    val = 0
    while n > 0:
        val += func(n % 10)
        n //= 10
    return val


if __name__ == '__main__':
    total = 0
    for i in range(2, 400000):
        if i == sum_digit_by(i, lambda n: n ** 5):
            print('>', i)
            total += i
    print(total)  # 443839
