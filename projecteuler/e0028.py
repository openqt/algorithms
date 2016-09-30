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


def spiral_grid(n):
    grid = [[0] * n for _ in range(n)]

    i = 1
    for loop in range(1, n, 2):
        row = 0
        col = loop - 1

        grid[row]
        while row != 0 and col != loop:
            if row == 0:
                col -= 1
            elif col == 0:
                row += 1
            elif row > 0:
                col += 1
            else:
                row -= 1
            grid[row][col] = i

            i+=1

    return grid


if __name__ == '__main__':
    grid = spiral_grid(5)
    for i in grid:
        print(i)
