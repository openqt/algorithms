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


def reverse(n):
    """reverse a number

    :param n: number
    :return: reversed number
    """
    val = 0
    while n > 0:
        val = val * 10 + n % 10
        n /= 10
    return val


def is_palindrome(n):
    """n is palindrome

    :param n: the number
    :return: True for palindrome
    """
    return n == reverse(n)


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
