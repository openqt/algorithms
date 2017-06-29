# coding=utf-8
"""
Consecutive prime sum
Problem 50

The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""
from __future__ import print_function
from utils import prime_sieve
from pe007_10001st_primes import is_prime


def _get(integrals):
    # 从积分列表里选出差值为质数并坐标差值最大的一组
    for i in range(len(integrals) - 1, 0, -1):
        for j in range(len(integrals) - i):
            if is_prime(integrals[i + j] - integrals[j]):
                return i, j, integrals[i + j] - integrals[j]


if __name__ == '__main__':
    # 构造积分图
    integrals = [0]
    primes = []
    n = 0
    for i in prime_sieve(1000000):
        primes.append(i)
        n += i
        if n > 1000000:
            break
        integrals.append(n)  # len = 547

    print(_get(integrals))  # (543, 3, 997651)
