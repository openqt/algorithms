#!/usr/bin/env python
# coding=utf-8
"""
Truncatable primes
Problem 37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from __future__ import print_function
from pe007_10001st_primes import prime, is_prime


def is_left_truncable_prime(n):
    i = n
    div = 1
    while i / div > 10:
        div *= 10

    while n > 10:
        n %= div
        if not is_prime(n):
            return False
        div /= 10
    return True


def is_right_truncable_prime(n):
    while n > 10:
        n //= 10
        if not is_prime(n):
            return False
    return True


if __name__ == '__main__':
    n = 0
    count = 0
    for i in prime():
        if i < 10:  # 2, 3, 5, 7 are not considered to be truncatable primes
            continue

        if is_right_truncable_prime(i) and is_left_truncable_prime(i):
            print('>', i)
            n += i

            count += 1
            if count == 11:  # only eleven primes that are both truncatable
                break
    print(n)  # 748317
