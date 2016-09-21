# coding=utf-8
"""
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
"""
from __future__ import print_function


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        integral = []
        for i in range(m):  # 积分图解法
            integral.append([1] * n)

        for i in range(1, m):
            for j in range(1, n):
                integral[i][j] = integral[i][j - 1] + integral[i - 1][j]
        return integral[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.uniquePaths(2, 3))  # 3
