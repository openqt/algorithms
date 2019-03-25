# coding=utf-8
import unittest

"""852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

Let's call an array `A` a _mountain_  if the following properties hold:

  * `A.length >= 3`
  * There exists some `0 < i < A.length - 1` such that `A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`

Given an array that is definitely a mountain, return any `i` such that `A[0] <
A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]`.

**Example 1:**

    
    
    **Input:** [0,1,0]
    **Output:** 1
    

**Example 2:**

    
    
    **Input:** [0,2,1,0]
    **Output:** 1

**Note:**

  1. `3 <= A.length <= 10000`
  2. ` 0 <= A[i] <= 10^6`
  3. A is a mountain, as defined above.


Similar Questions:
  Find Peak Element (find-peak-element)
"""


class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                return i - 1


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.peakIndexInMountainArray([0, 1, 0]), 1)
        self.assertEqual(s.peakIndexInMountainArray([0, 2, 1, 0]), 1)


if __name__ == "__main__":
    unittest.main()
