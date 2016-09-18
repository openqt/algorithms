# coding=utf-8
"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from __future__ import print_function
from e0003 import prime_by


if __name__ == '__main__':
    print(sum(prime_by(2000000)))  # 142913828922
