# coding=utf-8
import unittest

"""476. Number Complement
https://leetcode.com/problems/number-complement/description/

Given a positive integer, output its complement number. The complement
strategy is to flip the bits of its binary representation.

**Note:**  

  1. The given integer is guaranteed to fit within the range of a 32-bit signed integer.
  2. You could assume no leading zero bit in the integer’s binary representation.

**Example 1:**  

    
    
    **Input:** 5
    **Output:** 2
    **Explanation:** The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
    

**Example 2:**  

    
    
    **Input:** 1
    **Output:** 0
    **Explanation:** The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Similar Questions:

"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n, c = num, 0
        while n > 0:
            n >>= 1
            c += 1

        mask = 0xffffffff >> (32-c)
        return num ^ mask


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.findComplement(5), 2)
        self.assertEqual(s.findComplement(1), 0)


if __name__ == "__main__":
    unittest.main()
