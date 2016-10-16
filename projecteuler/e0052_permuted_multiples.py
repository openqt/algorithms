# coding=utf-8
"""
Permuted multiples
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""
from __future__ import print_function


def seq_int(n):
    """int to sequence

    :param n: number
    :return: digit sequence
    """
    seq = []
    while n > 0:
        seq.append(n % 10)
        n /= 10
    return seq


if __name__ == '__main__':
    for i in range(10000, 100000):
        n = 100000 + i
        if sorted(seq_int(n)) == sorted(seq_int(2 * n)) \
                == sorted(seq_int(3 * n)) == sorted(seq_int(5 * n)) \
                == sorted(seq_int(6 * n)) == sorted(seq_int(4 * n)):
            print(n, 2 * n, 3 * n, 4 * n, 5 * n, 6 * n)
            # 142857 285714 428571 571428 714285 857142
            break
