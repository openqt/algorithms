#!/usr/bin/env python
# coding=utf-8
"""
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20×20 grid?
"""
from __future__ import print_function
import numpy as np


if __name__ == '__main__':
    ROWS, COLS = 21, 21  # 相当于计算多一维的积分图
    grid = np.zeros((ROWS, COLS), dtype=np.uint)
    grid[0, :] = 1
    grid[:, 0] = 1

    for i in range(1, ROWS):
        for j in range(1, COLS):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    print(grid[-1][-1])
