# coding=utf-8
import unittest

"""125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/

Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

**Note:**  For the purpose of this problem, we define empty string as valid
palindrome.

**Example 1:**

    
    
    **Input:**  "A man, a plan, a canal: Panama"
    **Output:** true
    

**Example 2:**

    
    
    **Input:**  "race a car"
    **Output:** false


Similar Questions:
  Palindrome Linked List (palindrome-linked-list)
  Valid Palindrome II (valid-palindrome-ii)
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

        
class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(s.isPalindrome("race a car"))
        self.assertTrue(s.isPalindrome(".,"))
        self.assertTrue(s.isPalindrome(""))


if __name__ == "__main__":
    unittest.main()
