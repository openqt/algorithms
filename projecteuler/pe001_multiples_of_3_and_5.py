"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The add of these multiples is 23.

Find the add of all the multiples of 3 or 5 below 1000.
"""
from __future__ import print_function


def sum_to(n, stop):
    """sum up arithmetic progression by step

    :param n: arithmetic progression step
    :param stop: the maximum value
    :return: sum of arithmetic progression
    """
    # return sum(range(step, stop, step))
    N = stop / n
    return n * (N + 1) * N / 2


if __name__ == '__main__':
    print(sum_to(3, 999) + sum_to(5, 999) - sum_to(15, 999))  # 233168
