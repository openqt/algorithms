# coding=utf-8
"""
Powerful digit counts
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from __future__ import print_function, division

if __name__ == '__main__':
    total = 1  # 1^1

    n = 1
    while True:
        x = int(10 ** ((n - 1) / n) + 1)  # as ceil() except 1^1
        if x < 10:
            # print('>', n, range(x, 10))
            total += 10 - x
        else:
            break

        n += 1

    print(total)  # 49
