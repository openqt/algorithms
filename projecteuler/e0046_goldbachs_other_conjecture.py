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
from e0003_largest_prime_factor import prime_sieve


def _goldbach_conjecture_2(n, primes):
    for p in primes:
        if p >= n:
            break

        i = (n - p) // 2
        if int(int(i ** .5) ** 2) == i:
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
