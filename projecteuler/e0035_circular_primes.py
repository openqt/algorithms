# coding=utf-8
"""
Circular primes
Problem 35

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from __future__ import print_function
from e0003_largest_prime_factor import prime_sieve
from e0007_10001st_primes import is_prime


def circular_int(n):
    """circular int

    :param n: int
    :return: circular int
    """
    # yield n  # 不处理自身
    s = str(n)
    while True:
        s = s[1:] + s[0]
        val = int(s)
        if val == n:
            break
        yield val


def circular_prime(stop):
    """circular prime in a range

    :param stop:
    :return:
    """
    for i in prime_sieve(stop):
        for n in circular_int(i):
            if not is_prime(n):
                break
        else:
            yield i


if __name__ == '__main__':
    n = 0
    for i in circular_prime(1000000):
        print('>', i)
        n += 1
    print(n)
