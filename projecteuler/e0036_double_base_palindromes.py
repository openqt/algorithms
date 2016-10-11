# coding=utf-8
"""
Double-base palindromes
Problem 36

The decimal number, 585 = 1001001001/2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""
from __future__ import print_function
from e0004_largest_palindrome_product import is_palindrome


if __name__ == '__main__':
    n = 0
    for i in range(1, 1000000, 2):
        if is_palindrome(i) and is_palindrome(i, 2):
            print('>', i)
            n += i
    print(n)  # 872187
