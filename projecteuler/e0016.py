# coding=utf-8
"""
Power digit sum
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
from __future__ import print_function


def sum_digit(n):
    """sum digits of a number

    :param n:
    :return:
    """
    val = 0
    while n > 0:
        val += n % 10
        n /= 10
    return val


if __name__ == '__main__':
    print(sum_digit(2**1000))
