# coding=utf-8
"""
63. Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
from __future__ import print_function


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        integral = []
        for i in range(m):  # 积分图解法，遇到阻碍则其临近点不加
            integral.append([1] * n)

        if obstacleGrid[0][0] == 1:  # 按给定的阻碍条件设置边界值
            integral[0][0] = 0
        for i in range(m):
            if obstacleGrid[i][0] == 1:  # 纵向1之后全设为0
                for j in range(i, m):
                    integral[j][0] = 0
        for i in range(n):
            if obstacleGrid[0][i] == 1:  # 横向1之后全设为0
                for j in range(i, n):
                    integral[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:  # 阻碍
                    integral[i][j] = 0  # 积分图此区域设置为0，对下一点不增
                else:
                    integral[i][j] = integral[i][j - 1] + integral[i - 1][j]

        return integral[-1][-1]


if __name__ == '__main__':
    so = Solution()
    print(so.uniquePathsWithObstacles([[1]]))  # 0
    print(so.uniquePathsWithObstacles([[0, 1]]))  # 0
    print(so.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
