# coding=utf-8
import unittest

"""949. Largest Time for Given Digits
https://leetcode.com/problems/largest-time-for-given-digits/description/

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made,
return an empty string.



**Example 1:**

    
    
    **Input:** [1,2,3,4]
    **Output:** "23:41"
    

**Example 2:**

    
    
    **Input:** [5,5,5,5]
    **Output:** ""
    



**Note:**

  1. `A.length == 4`
  2. `0 <= A[i] <= 9`


Similar Questions:

"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
