# coding=utf-8
import unittest

"""231. Power of Two
https://leetcode.com/problems/power-of-two/description/

Given an integer, write a function to determine if it is a power of two.

**Example 1:**

    
    
    **Input:** 1
    **Output:** true 
    **Explanation:** 20 = 1
    

**Example 2:**

    
    
    **Input:** 16
    **Output:** true
    **Explanation:** 24 = 16

**Example 3:**

    
    
    **Input:** 218
    **Output:** false


Similar Questions:
  Number of 1 Bits (number-of-1-bits)
  Power of Three (power-of-three)
  Power of Four (power-of-four)
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n > 1:
            if n & 0x1 > 0: return False
            n >>= 1
        return True


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertFalse(s.isPowerOfTwo(-16))
        self.assertTrue(s.isPowerOfTwo(1))
        self.assertTrue(s.isPowerOfTwo(2))
        self.assertTrue(s.isPowerOfTwo(16))
        self.assertFalse(s.isPowerOfTwo(218))


if __name__ == "__main__":
    unittest.main()
