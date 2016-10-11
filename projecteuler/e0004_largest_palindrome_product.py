# coding=utf-8
"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from __future__ import print_function


def reverse_int(n, base=10):
    """reverse a number

    :param n: number
    :param base:
    :return: reversed number
    """
    val = 0
    while n > 0:
        val = val * base + n % base
        n /= base
    return val


def is_palindrome(n, base=10):
    """n is palindrome

    :param n: the number
    :param base:
    :return: True for palindrome
    """
    return n == reverse_int(n, base)


if __name__ == '__main__':
    a = b = c = 0
    for i in range(999, 99, -1):
        for j in range(999, i, -1):
            val = i * j
            if val < c:
                break
            if is_palindrome(val):
                a, b, c = i, j, val

    print('%d x %d = %d' % (a, b, c))  # 913 x 993 = 906609
