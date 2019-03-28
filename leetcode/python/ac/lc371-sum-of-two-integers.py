# coding=utf-8
import unittest

"""371. Sum of Two Integers
https://leetcode.com/problems/sum-of-two-integers/description/

Calculate the sum of two integers _a_ and _b_ , but you are **not allowed** to
use the operator `+` and `-`.

**Example:**  
Given _a_ = 1 and _b_ = 2, return 3.

**Credits:**  
Special thanks to [@fujiaozhu](https://discuss.leetcode.com/user/fujiaozhu)
for adding this problem and creating all test cases.


Similar Questions:
  Add Two Numbers (add-two-numbers)
"""


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            a, b = (a ^ b) & 0xffffffff, ((a & b) << 1) & 0xffffffff
        return a if a <= 0x7fffffff else ~(a ^ 0xffffffff)


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.getSum(-12, -8), -20)
        self.assertEqual(s.getSum(-1, 1), 0)
        self.assertEqual(s.getSum(1, 2), 3)


if __name__ == "__main__":
    unittest.main()
