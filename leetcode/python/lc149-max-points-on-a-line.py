# coding=utf-8
import unittest

"""149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/description/

Given _n_ points on a 2D plane, find the maximum number of points that lie on
the same straight line.

**Example 1:**

    
    
    **Input:** [[1,1],[2,2],[3,3]]
    **Output:** 3
    **Explanation:**
    ^
    |
    |         o
    |     o
    |  o  
    +------------->
    0  1  2  3  4
    

**Example 2:**

    
    
    **Input:** [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    **Output:** 4
    **Explanation:**
    ^
    |
    |  o
    |      o        o
    |        o
    |  o        o
    +------------------->
    0  1  2  3  4  5  6


Similar Questions:
  Line Reflection (line-reflection)
"""


# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
