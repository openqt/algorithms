#!/usr/bin/env python
# coding=utf-8
"""
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from __future__ import print_function


def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def factorial(n):
    if n < 1:  # 0! = 1
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


if __name__ == '__main__':
    print(sum_digits(factorial(100)))  # 648
