# coding=utf-8
import unittest

"""633. Sum of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers/description/

Given a non-negative integer `c`, your task is to decide whether there're two
integers `a` and `b` such that a2 \+ b2 = c.

**Example 1:**  

    
    
    **Input:** 5
    **Output:** True
    **Explanation:** 1 * 1 + 2 * 2 = 5
    

**Example 2:**  

    
    
    **Input:** 3
    **Output:** False


Similar Questions:
  Valid Perfect Square (valid-perfect-square)
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        vals = {i * i for i in range(int(c ** .5)+1)}
        for i in vals:
            if (c - i) in vals:
                return True
        return False


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.judgeSquareSum(5))
        self.assertFalse(s.judgeSquareSum(3))
        self.assertTrue(s.judgeSquareSum(4))


if __name__ == "__main__":
    unittest.main()
