# coding=utf-8
import unittest

"""463. Island Perimeter
https://leetcode.com/problems/island-perimeter/description/

You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water. Grid cells are connected
horizontally/vertically (not diagonally). The grid is completely surrounded by
water, and there is exactly one island (i.e., one or more connected land
cells). The island doesn't have "lakes" (water inside that isn't connected to
the water around the island). One cell is a square with side length 1. The
grid is rectangular, width and height don't exceed 100. Determine the
perimeter of the island.

**Example:**

    
    
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
    
    Answer: 16
    Explanation: The perimeter is the 16 yellow stripes in the image below:
    ![](/static/images/problemset/island.png)


Similar Questions:
  Max Area of Island (max-area-of-island)
  Flood Fill (flood-fill)
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        S = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    S.add((row, col))
        P = 0
        for (r, c) in S:
            P += 4
            for i in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if i in S:
                    P -= 1
        return P


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16)


if __name__ == "__main__":
    unittest.main()
