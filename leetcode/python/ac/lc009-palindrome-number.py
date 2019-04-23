# coding=utf-8
import unittest

"""9. Palindrome Number
https://leetcode.com/problems/palindrome-number/description/

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

**Example 1:**

    
    
    **Input:** 121
    **Output:** true
    

**Example 2:**

    
    
    **Input:** -121
    **Output:** false
    **Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    

**Example 3:**

    
    
    **Input:** 10
    **Output:** false
    **Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.
    

**Follow up:**

Coud you solve it without converting the integer to a string?


Similar Questions:
  Palindrome Linked List (palindrome-linked-list)
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type n: int
        :rtype: bool
        """
        if x < 0: return False
        v, n = 0, x
        while n > 0:
            v = v * 10 + n % 10
            n //= 10
        return v == x


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(121))
        self.assertFalse(s.isPalindrome(-121))
        self.assertFalse(s.isPalindrome(10))


if __name__ == "__main__":
    unittest.main()
