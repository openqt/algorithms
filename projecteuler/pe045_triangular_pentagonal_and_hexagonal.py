#!/usr/bin/env python
# coding=utf-8
"""
Triangular, pentagonal, and hexagonal
Problem 45

Triangle, pentagonal, and hexagonal numbers are generated by the following
formulae:

    Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
    Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
    Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
from __future__ import print_function
from pe012_highly_divisible_triangular_number import triangle_number
from pe044_pentagon_numbers import pentagonal_number


def hexagonal_number(start=1, count=-1):
    """hexagonal sequence

    :param start:
    :param count:
    :return:
    """
    while count != 0:
        hexagonal_number.func_dict['n'] = start

        count -= 1
        yield start * (2 * start - 1)
        start += 1


if __name__ == '__main__':
    ti = triangle_number(start=285 + 1)
    pi = pentagonal_number(start=165)
    hi = hexagonal_number(start=143)

    t = ti.next()
    p = pi.next()
    h = hi.next()
    while True:
        while p < t:
            p = pi.next()

        while h < t:
            h = hi.next()

        if t == p == h:
            print(t)  # 1533776805
            break
        else:
            t = ti.next()
