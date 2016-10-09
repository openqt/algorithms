"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from __future__ import print_function


def prime_sieve(n, reverse=False):
    """prime sequence to n

    :param n: the maximum range
    :param reverse: reverse prime sequence
    :return: prime sequence between [2, n]
    """
    marker = bytearray(n >> 1)

    for i in range(3, int(n ** .5 + 1), 2):
        if marker[i >> 1] == 0:  # prime
            for j in range(i * i, n, 2 * i):
                marker[j >> 1] = 1

    if not reverse:
        yield 2
        _range = range(1, len(marker))
    else:
        _range = range(len(marker) - 1, 0, -1)

    for i in _range:
        if marker[i] == 0:
            yield 2 * i + 1

    if reverse:
        yield 2


if __name__ == '__main__':
    val = 600851475143
    for i in prime_sieve(int(val ** .5), True):
        if val % i == 0:
            print(i)  # 6857
            break
