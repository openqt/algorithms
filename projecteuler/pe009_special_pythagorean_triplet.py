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


def triplet_by(n):
    for a in range(3, n / 3):
        for b in range(a + 1, (n - a) / 2):
            c = n - b - a
            yield (a, b, c)


if __name__ == '__main__':
    for a, b, c in triplet_by(1000):
        if a * a + b * b == c * c:  # 200 x 375 x 425 = 31875000
            print('%d x %d x %d = %d' % (a, b, c, a * b * c))
            break
