# coding=utf-8
"""
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""
from __future__ import print_function
from utils import prime_sieve


def is_square_number(n):
    """whether a number is a perfect square

    :param n:
    :return:
    """
    # the last hex digit of a perfect square must be 0, 1, 4 or 9
    if n < 0 or n & 0xF not in (0, 1, 4, 9):
        return False
    return int(n ** .5 + .5) ** 2 == n


def _goldbach_conjecture_2(n, primes):
    for p in primes:
        if p >= n:
            break

        if is_square_number((n - p) // 2):
            return True
    return False


if __name__ == '__main__':
    primes = list(i for i in prime_sieve(10000))
    caches = set(primes)

    n = 9
    while True:
        if n not in caches:  # not a prime
            if not _goldbach_conjecture_2(n, primes):
                print(n)  # 5777
                break
        n += 2
