# coding=utf-8
import unittest

"""73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/description/

Given a _m_ x _n_ matrix, if an element is 0, set its entire row and column to
0. Do it [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm).

**Example 1:**

    
    
    **Input:** 
    [
       [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    **Output:** 
    [
       [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    

**Example 2:**

    
    
    **Input:** 
    [
       [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    **Output:** 
    [
       [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    

**Follow up:**

  * A straight forward solution using O( _m_ _n_ ) space is probably a bad idea.
  * A simple improvement uses O( _m_ \+ _n_ ) space, but still not the best solution.
  * Could you devise a constant space solution?


Similar Questions:
  Game of Life (game-of-life)
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
