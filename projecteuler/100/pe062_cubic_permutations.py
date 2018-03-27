#!/usr/bin/env python
# coding=utf-8
"""
Cubic permutations
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
"""
from __future__ import print_function

if __name__ == '__main__':
    caches = {}
    for i in range(1000, 10000):
        caches.setdefault(tuple(sorted(str(i ** 3))), []).append(i)

    for k in caches:
        if len(caches[k]) >= 5:
            print(k, caches[k], caches[k][0] ** 3)  # 127035954683
