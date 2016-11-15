# coding=utf-8
"""
Number spiral diagonals
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""
from __future__ import print_function


def spiral_grid(n, clockwise=True):
    """build spiral gird clockwise or anticlockwise

    :param n: dimension
    :param clockwise: True for clockwise and False for anticlockwise
    :return: spiral gird
    """
    grid = [[1] * n for _ in range(n)]

    row = 0 if clockwise else n - 1
    col = n - 1

    val = n ** 2
    while val > 1:
        for i in range(4):  # direction
            for j in range(n - 1):  # value 4*(n-1)
                grid[row][col] = val
                val -= 1

                if i == 0:  # up
                    col -= 1
                elif i == 1:  # left
                    row += 1 if clockwise else -1
                elif i == 2:  # down
                    col += 1
                elif i == 3:  # right
                    row += -1 if clockwise else 1
                else:
                    raise ValueError()

        row += 1 if clockwise else -1
        col -= 1
        n -= 2  # n仅作计数用
    return grid


if __name__ == '__main__':
    n = 1001
    grid = spiral_grid(n)
    print(sum(grid[i][i] + grid[i][n - i - 1] for i in range(n)) - 1)  # 669171001
