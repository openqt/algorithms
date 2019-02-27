# coding=utf-8
import unittest

"""263. Ugly Number
https://leetcode.com/problems/ugly-number/description/

Write a program to check whether a given number is an ugly number.

Ugly numbers are **positive numbers** whose prime factors only include `2, 3,
5`.

**Example 1:**

    
    
    **Input:** 6
    **Output:** true
    **Explanation:** 6 = 2 × 3

**Example 2:**

    
    
    **Input:** 8
    **Output:** true
    **Explanation:** 8 = 2 × 2 × 2
    

**Example 3:**

    
    
    **Input:** 14
    **Output:** false 
    **Explanation:**14 is not ugly since it includes another prime factor 7.
    

**Note:**

  1. `1` is typically treated as an ugly number.
  2. Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].


Similar Questions:
  Happy Number (happy-number)
  Count Primes (count-primes)
  Ugly Number II (ugly-number-ii)
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1: return False
        for i in (2, 3, 5):
            while num % i == 0:
                num /= i
        return num == 1


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isUgly(6))
        self.assertTrue(s.isUgly(8))
        self.assertFalse(s.isUgly(17))


if __name__ == "__main__":
    unittest.main()
