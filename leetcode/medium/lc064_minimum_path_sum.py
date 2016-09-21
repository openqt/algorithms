# coding=utf-8
"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
from __future__ import print_function


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        # 计算积分图
        integral = []
        for i in range(m):
            integral.append([grid[0][0]] * n)

        for i in range(1, n):
            integral[0][i] = grid[0][i] + integral[0][i - 1]
        for i in range(1, m):
            integral[i][0] = grid[i][0] + integral[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                integral[i][j] = min(integral[i][j - 1],
                                     integral[i - 1][j]) + grid[i][j]

        return integral[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.minPathSum([[1]]))  # 1
    print(so.minPathSum([[1, 2], [1, 1]]))  # 1
