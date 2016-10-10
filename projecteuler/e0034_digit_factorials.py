# coding=utf-8
"""
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from __future__ import print_function
from e0020_factorial_digit_sum import factorial
from e0030_digit_fifth_powers import sum_digit_by


def _factorial_index(n):
    d = _factorial_index.__dict__
    if not d:
        for i in range(10):
            d[i] = factorial(i)
    return d[n]


if __name__ == '__main__':
    total = 0
    for i in range(3, 2500000):
        if i == sum_digit_by(i, _factorial_index):
            print('>', i)
            total += i
    print(total)  # 40730
