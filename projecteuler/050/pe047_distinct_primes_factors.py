#!/usr/bin/env python
# coding=utf-8
"""
Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?
"""
from __future__ import print_function
from pe012_highly_divisible_triangular_number import prime_factors


def _distinct_prime_factors(args):
    for i in range(args[1]):
        n = prime_factors(args[0])
        args[0] += 1

        if len(n) != args[1]:
            return False
    return True


if __name__ == '__main__':
    args = [10, 4]  # start, length
    while not _distinct_prime_factors(args):
        pass
    print(args[0] - args[1])  # 134043
