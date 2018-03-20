#!/usr/bin/env python
# coding=utf-8
"""
Combinatoric selections
Problem 53

There are exactly ten ways of selecting three from five, 12345:

    123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

    nCr = n!/r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
greater than one-million?
"""
from __future__ import print_function
from pe020_factorial_digit_sum import factorial


def calc_combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def t():
    counter = 0
    for n in range(23, 101):
        d = n
        r = 1
        while d < 1000000 and r <= int(n / 2):
            d = d * (n - r) / (r + 1)
            r += 1
        counter += n - 2 * r + 1
    print(counter)


if __name__ == '__main__':
    total = 0
    for n in range(20, 101):
        for r in range(1, n // 2):
            if calc_combination(n, r) > 1000000:
                total += n - 2 * r + 1
                break
    print(total)  # 4075
