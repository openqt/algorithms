# coding=utf-8
import unittest

"""693. Binary Number with Alternating Bits
https://leetcode.com/problems/binary-number-with-alternating-bits/description/

Given a positive integer, check whether it has alternating bits: namely, if
two adjacent bits will always have different values.

**Example 1:**  

    
    
    **Input:** 5
    **Output:** True
    **Explanation:**
    The binary representation of 5 is: 101
    

**Example 2:**  

    
    
    **Input:** 7
    **Output:** False
    **Explanation:**
    The binary representation of 7 is: 111.
    

**Example 3:**  

    
    
    **Input:** 11
    **Output:** False
    **Explanation:**
    The binary representation of 11 is: 1011.
    

**Example 4:**  

    
    
    **Input:** 10
    **Output:** True
    **Explanation:**
    The binary representation of 10 is: 1010.


Similar Questions:
  Number of 1 Bits (number-of-1-bits)
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = n & 1
        while n > 0:
            n >>= 1
            flag = int(not flag)
            if n & 1 != flag:
                return False
        return True


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertFalse(s.hasAlternatingBits(8))
        self.assertTrue(s.hasAlternatingBits(5))
        self.assertFalse(s.hasAlternatingBits(7))
        self.assertFalse(s.hasAlternatingBits(11))
        self.assertTrue(s.hasAlternatingBits(10))


if __name__ == "__main__":
    unittest.main()
