# coding=utf-8
import unittest

"""766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/description/

A matrix is _Toeplitz_ if every diagonal from top-left to bottom-right has the
same element.

Now given an `M x N` matrix, return `True` if and only if the matrix is
_Toeplitz_.  


**Example 1:**

    
    
    **Input:** matrix = [
      [1,2,3,4],
      [5,1,2,3],
      [9,5,1,2]
    ]
    **Output:** True
    **Explanation:**
    In the above grid, the  diagonals are:
    "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
    In each diagonal all elements are the same, so the answer is True.
    

**Example 2:**

    
    
    **Input:** matrix = [
      [1,2],
      [2,2]
    ]
    **Output:** False
    **Explanation:**
    The diagonal  "[1, 2]" has different elements.
    

  
**Note:**

  1. `matrix` will be a 2D array of integers.
  2. `matrix` will have a number of rows and columns in range `[1, 20]`.
  3. `matrix[i][j]` will be integers in range `[0, 99]`.

  
**Follow up:**

  1. What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
  2. What if the matrix is so large that you can only load up a partial row into the memory at once?


Similar Questions:
  Valid Word Square (valid-word-square)
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix: return True

        for i in range(len(matrix)):
            if not self._toeplitz(matrix, i, 0): return False

        for j in range(len(matrix[0])):
            if not self._toeplitz(matrix, 0, j): return False

        return True

    def _toeplitz(self, M, x, y):
        i, j = x + 1, y + 1
        while i < len(M) and j < len(M[0]):
            if M[i][j] != M[x][y]:
                return False
            i += 1
            j += 1
        return True


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isToeplitzMatrix([
            [1, 2, 3, 4],
            [5, 1, 2, 3],
            [9, 5, 1, 2]]))
        self.assertFalse(s.isToeplitzMatrix([
            [1, 2],
            [2, 2]]))


if __name__ == "__main__":
    unittest.main()
