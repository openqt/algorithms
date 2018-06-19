import unittest

"""463. Island Perimeter
https://leetcode.com/problems/island-perimeter/description/

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water,
and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.

Example:

    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]

Answer: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
[!lc463_island.png](island)
"""


class Solution(unittest.TestCase):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        p = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    p += self.countWater(x, y)
        return p

    def countWater(self, x, y):
        count = 4
        count -= self.waterOrIsland(x - 1, y)
        count -= self.waterOrIsland(x + 1, y)
        count -= self.waterOrIsland(x, y - 1)
        count -= self.waterOrIsland(x, y + 1)
        return count

    def waterOrIsland(self, x, y):
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[x]):
            return self.grid[x][y]
        return 0

    def test(self):
        self.assertEqual(self.islandPerimeter([[1], [0]]), 4)
        self.assertEqual(self.islandPerimeter([[0, 1, 0, 0],
                                               [1, 1, 1, 0],
                                               [0, 1, 0, 0],
                                               [1, 1, 0, 0]]), 16)


if __name__ == "__main__":
    unittest.main()
