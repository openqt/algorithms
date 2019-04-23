# coding=utf-8
import unittest

"""680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/description/

Given a non-empty string `s`, you may delete **at most** one character. Judge
whether you can make it a palindrome.

**Example 1:**  

    
    
    **Input:** "aba"
    **Output:** True
    

**Example 2:**  

    
    
    **Input:** "abca"
    **Output:** True
    **Explanation:** You could delete the character 'c'.
    

**Note:**  

  1. The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


Similar Questions:
  Valid Palindrome (valid-palindrome)
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def palindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return i, j
                i += 1
                j -= 1
            return -1, -1

        i, j = palindrome(s)
        if i > -1:
            return palindrome(s[i + 1:j + 1]) == (-1, -1) or palindrome(s[i:j]) == (-1, -1)
        return True


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.validPalindrome("aba"), True)
        self.assertEqual(s.validPalindrome("abca"), True)


if __name__ == "__main__":
    unittest.main()
