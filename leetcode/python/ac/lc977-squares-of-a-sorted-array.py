# coding=utf-8
import unittest

"""977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/description/

Given an array of integers `A` sorted in non-decreasing order, return an array
of the squares of each number, also in sorted non-decreasing order.



**Example 1:**

    
    
    **Input:** [-4,-1,0,3,10]
    **Output:** [0,1,9,16,100]
    

**Example 2:**

    
    
    **Input:** [-7,-3,2,3,11]
    **Output:** [4,9,9,49,121]
    



**Note:**

  1. ` 1 <= A.length <= 10000`
  2. `-10000 <= A[i] <= 10000`
  3. `A` is sorted in non-decreasing order.


Similar Questions:

"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(i**2 for i in A)


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(s.sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])


if __name__ == "__main__":
    unittest.main()
