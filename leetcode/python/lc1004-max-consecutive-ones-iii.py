# coding=utf-8
import unittest

"""1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/description/

Given an array `A` of 0s and 1s, we may change up to `K` values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



**Example 1:**

    
    
    **Input:** A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
    **Output:** 6
    **Explanation:**
    [1,1,1,0,0, _ **1** ,1,1,1,1, **1**_ ]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

**Example 2:**

    
    
    **Input:** A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
    **Output:** 10
    **Explanation:**
    [0,0, _1,1, **1** , **1** ,1,1,1, **1** ,1,1_,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
    



**Note:**

  1. `1 <= A.length <= 20000`
  2. `0 <= K <= A.length`
  3. `A[i]` is `0` or `1`


Similar Questions:
  Longest Substring with At Most K Distinct Characters (longest-substring-with-at-most-k-distinct-characters)
  Longest Repeating Character Replacement (longest-repeating-character-replacement)
  Max Consecutive Ones (max-consecutive-ones)
  Max Consecutive Ones II (max-consecutive-ones-ii)
"""


class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        

class T(unittest.TestCase):
    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
