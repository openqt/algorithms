# coding=utf-8
import unittest

"""367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/description/

Given a positive integer _num_ , write a function which returns True if _num_
is a perfect square else False.

**Note:** **Do not** use any built-in library function such as `sqrt`.

**Example 1:**

    
    
    Input: 16
    Returns: True
    

**Example 2:**

    
    
    Input: 14
    Returns: False
    

**Credits:**  
Special thanks to [@elmirap](https://discuss.leetcode.com/user/elmirap) for
adding this problem and creating all test cases.


Similar Questions:
  Sqrt(x) (sqrtx)
  Sum of Square Numbers (sum-of-square-numbers)
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a, b = 0, num
        while a <= b:
            m = (b + a) // 2
            if m * m > num:
                b = m - 1
            elif m * m < num:
                a = m + 1
            else:
                return True
        return False


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isPerfectSquare(1))
        self.assertTrue(s.isPerfectSquare(16))
        self.assertFalse(s.isPerfectSquare(14))


if __name__ == "__main__":
    unittest.main()
