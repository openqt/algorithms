"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math


def prime_by(n, reverse=False):
    """
    prime sequence to n
    :param n: the maximum range
    :param reverse: reverse prime sequence
    :return: prime sequence between [2, n]
    """
    marker = bytearray(n)
    for i in range(2, int(math.sqrt(n))):
        if marker[i] == 0:
            for j in range(i * i, n, i):
                marker[j] = 1

    _r = range(len(marker) - 1, 1, -1) if reverse else range(2, len(marker))
    for i in _r:
        if marker[i] == 0:
            yield i


val = 600851475143
for i in prime_by(int(math.sqrt(val)), True):
    if val % i == 0:
        print(i)
        break
