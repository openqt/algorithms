#!/usr/bin/env python
# coding=utf-8
"""
Prime summations
Problem 77

It is possible to write ten as the sum of primes in exactly five different ways:

    7 + 3
    5 + 5
    5 + 3 + 2
    3 + 3 + 2 + 2
    2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five
thousand different ways?
"""
from __future__ import print_function
from utils import prime_sieve, different_ways

if __name__ == '__main__':
    primes, n = list(prime_sieve(1000)), 10
    while True:
        if different_ways(n, primes) > 5000:
            print(n, different_ways(n, primes))  # 71 5007
            break
        n += 1
