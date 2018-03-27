#!/usr/bin/env python
# coding=utf-8
"""
Singular integer right triangles
Problem 75

It turns out that 12 cm is the smallest length of wire that can be bent to form
an integer sided right angle triangle in exactly one way, but there are many
more examples.

    12 cm: (3,4,5)
    24 cm: (6,8,10)
    30 cm: (5,12,13)
    36 cm: (9,12,15)
    40 cm: (8,15,17)
    48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
integer sided right angle triangle, and other lengths allow more than one
solution to be found; for example, using 120 cm it is possible to form exactly
three different integer sided right angle triangles.

    120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000
can exactly one integer sided right angle triangle be formed?
"""
from __future__ import print_function
from pe005_smallest_multiple import GCD


def pythagorean_triplet_by(p):
    """Generating right angle triangles by perimeter
        a = k(m^2 – n^2)
        b = 2kmn
        c = k(m^2 + n^2)

    :param p: perimeter
    :return:
    """
    for m in range(2, int(p ** .5)):
        for n in range(1, m):  # m > n > 0
            # gcd(m, n) = 1 and exactly one of m, n even
            if (m + n) % 2 == 1 and GCD(m, n) == 1:
                k = 1
                while True:
                    a = k * (m * m - n * n)
                    b = k * (2 * m * n)
                    c = k * (m * m + n * n)
                    if a + b + c >= p:
                        break
                    k += 1
                    yield a, b, c


if __name__ == '__main__':
    vals = {}
    for a, b, c in pythagorean_triplet_by(1500001):
        p = a + b + c
        vals[p] = vals.get(p, 0) + 1

    print('caches:', len(vals))
    print(sum(1 for i in vals.values() if i == 1))
