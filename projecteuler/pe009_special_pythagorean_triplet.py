#!/usr/bin/env python
# coding=utf-8
"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from __future__ import print_function
from pe005_smallest_multiple import GCD

# def triplet_by(n):
#     for a in range(3, n / 3):
#         for b in range(a + 1, (n - a) / 2):
#             c = n - b - a
#             yield (a, b, c)


def pythagorean_triplet(n):
    """Generating right angle triangle which a + b + c = n

    :param n:
    :return:
    """
    n2 = n / 2
    for m in range(2, int(n2 ** .5) + 1):
        if n2 % m == 0:
            sm = n2 / m
            while sm % 2 == 0:  # removing all factors 2
                sm /= 2

            for k in range(m + 1 + m % 2, min(2 * m, sm) + 1, 2):
                if sm % k == 0 and GCD(k, m) == 1:
                    n = k - m
                    d = n2 / (k * m)

                    a = d * (m * m - n * n)
                    b = 2 * d * m * n
                    c = d * (m * m + n * n)
                    yield a, b, c


if __name__ == '__main__':
    for a, b, c in pythagorean_triplet(1000):
        print(a, b, c, a * b * c)  # 31875000
