# coding=utf-8
import unittest

"""7. Reverse Integer
https://leetcode.com/problems/reverse-integer/description/

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**

    
    
    **Input:** 123
    **Output:** 321
    

**Example 2:**

    
    
    **Input:** -123
    **Output:** -321
    

**Example 3:**

    
    
    **Input:** 120
    **Output:** 21
    

**Note:**  
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [ −2^31,  2^31 − 1]. For the purpose of
this problem, assume that your function returns 0 when the reversed integer
overflows.


Similar Questions:
  String to Integer (atoi) (string-to-integer-atoi)
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        val = 0
        if x < 0:
            minus = True
            x = -x
        else:
            minus = False

        while x != 0:
            val = val * 10 + x % 10
            x //= 10

        if val > 2**31:
            val = 0

        if minus:
            val = -val
        return val

        
class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.reverse(123), 321)
        self.assertEqual(s.reverse(-123), -321)
        self.assertEqual(s.reverse(120), 21)


if __name__ == "__main__":
    unittest.main()
