# coding=utf-8
import unittest

"""1018. Binary Prefix Divisible By 5
https://leetcode.com/problems/binary-prefix-divisible-by-5/description/

Given an array `A` of `0`s and `1`s, consider `N_i`: the i-th subarray from
`A[0]` to `A[i]` interpreted as a binary number (from most-significant-bit to
least-significant-bit.)

Return a list of booleans `answer`, where `answer[i]` is `true` if and only if
`N_i` is divisible by 5.

**Example 1:**

    
    
    **Input:** [0,1,1]
    **Output:** [true,false,false]
    **Explanation:**
    The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.
    

**Example 2:**

    
    
    **Input:** [1,1,1]
    **Output:** [false,false,false]
    

**Example 3:**

    
    
    **Input:** [0,1,1,1,1,1]
    **Output:** [true,false,false,false,true,false]
    

**Example 4:**

    
    
    **Input:** [1,1,1,0,1]
    **Output:** [false,false,false,false,false]
    



**Note:**

  1. `1 <= A.length <= 30000`
  2. `A[i]` is `0` or `1`


Similar Questions:

"""


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        

class T(unittest.TestCase):
    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
