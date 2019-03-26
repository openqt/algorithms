# coding=utf-8
import unittest

"""509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/description/

The  **Fibonacci numbers** , commonly denoted `F(n)` form a sequence, called
the  **Fibonacci sequence** , such that each number is the sum of the two
preceding ones, starting from `0` and `1`. That is,

    
    
    F(0) = 0,   F(1) = 1
    F(N) = F(N - 1) + F(N - 2), for N > 1.
    

Given `N`, calculate `F(N)`.



**Example 1:**

    
    
    **Input:** 2
    **Output:** 1
    **Explanation:** F(2) = F(1) + F(0) = 1 + 0 = 1.
    

**Example 2:**

    
    
    **Input:** 3
    **Output:** 2
    **Explanation:** F(3) = F(2) + F(1) = 1 + 1 = 2.
    

**Example 3:**

    
    
    **Input:** 4
    **Output:** 3
    **Explanation:** F(4) = F(3) + F(2) = 2 + 1 = 3.
    



**Note:**

0 ≤ `N` ≤ 30.


Similar Questions:
  Climbing Stairs (climbing-stairs)
  Split Array into Fibonacci Sequence (split-array-into-fibonacci-sequence)
  Length of Longest Fibonacci Subsequence (length-of-longest-fibonacci-subsequence)
"""


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 1: return N
        a, b = 0, 1
        for i in range(N - 1):
            a, b = b, a + b
        return b


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.fib(2), 1)
        self.assertEqual(s.fib(4), 3)


if __name__ == "__main__":
    unittest.main()
