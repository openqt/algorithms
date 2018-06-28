# coding=utf-8
import unittest

"""130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions/description/

Given a 2D board containing `'X'` and `'O'` ( **the letter O** ), capture all
regions surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded
region.

**Example:**

    
    
    X X X X
    X O O X
    X X O X
    X O X X
    

After running your function, the board should be:

    
    
    X X X X
    X X X X
    X X X X
    X O X X
    

**Explanation:**

Surrounded regions shouldn't be on the border, which means that any `'O'` on
the border of the board are not flipped to `'X'`. Any `'O'` that is not on the
border and it is not connected to an `'O'` on the border will be flipped to
`'X'`. Two cells are connected if they are adjacent cells connected
horizontally or vertically.


Similar Questions:
  Number of Islands (number-of-islands)
  Walls and Gates (walls-and-gates)
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
