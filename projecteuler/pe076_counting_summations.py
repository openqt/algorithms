# coding=utf-8
"""
Counting summations
Problem 76

It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?
"""
from __future__ import print_function
from utils import different_ways

if __name__ == '__main__':
    print(different_ways(100, range(1, 100)))  # 190569291

# Nice work, openqt, you've just advanced to Level 3 .
# 17771 members (2.72%) have made it this far.
