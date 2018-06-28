# coding=utf-8
import unittest

"""63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/description/

A robot is located at the top-left corner of a _m_ x _n_ grid (marked  'Start'
in the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

Now consider if some obstacles are added to the grids. How many unique paths
would there be?

![](https://leetcode.com/static/images/problemset/robot_maze.png)

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** _m_ and _n_ will be at most 100.

**Example 1:**

    
    
    **Input:** [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    **Output:** 2
    **Explanation:**
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right - > Right -> Down -> Down
    2. Down -> Down -> Right -> Right


Similar Questions:
  Unique Paths (unique-paths)
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
