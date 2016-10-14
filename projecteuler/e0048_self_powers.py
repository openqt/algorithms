# coding=utf-8
"""
Self powers
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
from __future__ import print_function

if __name__ == '__main__':
    n = 1
    last = 0
    while n <= 1000:
        last += n**n % 10000000000
        n += 1

    print(last % 10000000000, last)  # 9110846700
