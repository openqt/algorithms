# coding=utf-8
import unittest

"""992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/description/

Given an array `A` of positive integers, call a (contiguous, not necessarily
distinct) subarray of `A` _good_ if the number of different integers in that
subarray is exactly `K`.

(For example, `[1,2,3,1,2]` has `3` different integers: `1`, `2`, and `3`.)

Return the number of good subarrays of `A`.



**Example 1:**

    
    
    **Input:** A = [1,2,1,2,3], K = 2
    **Output:** 7
    **Explanation:** Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
    

**Example 2:**

    
    
    **Input:** A = [1,2,1,3,4], K = 3
    **Output:** 3
    **Explanation:** Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
    



**Note:**

  1. `1 <= A.length <= 20000`
  2. `1 <= A[i] <= A.length`
  3. `1 <= K <= A.length`


Similar Questions:

"""


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
