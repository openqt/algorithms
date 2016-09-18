"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The add of these multiples is 23.

Find the add of all the multiples of 3 or 5 below 1000.
"""
from __future__ import print_function


def sum_by(step, stop=1000):
    """sum up arithmetic progression by step

    :param step: arithmetic progression step
    :param stop: the maximum value
    :return: sum of arithmetic progression
    """
    return sum(range(step, stop, step))


if __name__ == '__main__':
    print(sum_by(3) + sum_by(5) - sum_by(15))  # 233168
