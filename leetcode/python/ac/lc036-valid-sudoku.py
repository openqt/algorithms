# coding=utf-8
import unittest

"""36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
validated  **according to the following rules** :

  1. Each row must contain the digits `1-9` without repetition.
  2. Each column must contain the digits `1-9` without repetition.
  3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-
L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)  
A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with
the character `'.'`.

**Example 1:**

    
    
    **Input:**
    [
      [ "5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    **Output:** true
    

**Example 2:**

    
    
    **Input:**
    [
       ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    **Output:** false
    **Explanation:** Same as Example 1, except with the **5** in the top left corner being 
        modified to **8**. Since there are two 8 's in the top left 3x3 sub-box, it is invalid.
    

**Note:**

  * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
  * Only the filled cells need to be validated according to the mentioned rules.
  * The given board contain only digits `1-9` and the character `'.'`.
  * The given board size is always `9x9`.


Similar Questions:
  Sudoku Solver (sudoku-solver)
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board
        for i in range(9):
            if not (self._check(self._row(i)) and
                    self._check(self._col(i)) and
                    self._check(self._grid(i))):
                return False
        return True

    def _check(self, cells):
        cache = set()
        for i in cells:
            if i == '.':
                continue
            if i in cache:
                return False
            else:
                cache.add(i)
        return True

    def _row(self, row):
        for i in range(9):
            yield self.board[row][i]

    def _col(self, col):
        for i in range(9):
            yield self.board[i][col]

    def _grid(self, cell):
        POS = [
            (1, 1), (1, 4), (1, 7),
            (4, 1), (4, 4), (4, 7),
            (7, 1), (7, 4), (7, 7),
        ]
        row, col = POS[cell]
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                yield self.board[i][j]


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isValidSudoku([
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]))
        self.assertFalse(s.isValidSudoku([
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]))


if __name__ == "__main__":
    unittest.main()
