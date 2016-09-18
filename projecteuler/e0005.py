"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
from __future__ import print_function


def GCD(a, b):
    """greatest common divisor (G.C.D.)

    :param a: a
    :param b: b
    :return: GCD
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def LCM(a, b):
    """lowest common multiple (L.C.M.)

    :param a: a
    :param b: b
    :return: LCM
    """
    return a * b / GCD(a, b)


if __name__ == '__main__':
    print(reduce(LCM, range(1, 11)))  # 2520
    print(reduce(LCM, range(1, 21)))  # 232792560
