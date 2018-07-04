# coding=utf-8
import unittest

"""5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string **s** , find the longest palindromic substring in **s**. You
may assume that the maximum length of **s** is 1000.

**Example 1:**

    
    
    **Input:**  "babad"
    **Output:**  "bab"
    **Note:**  "aba" is also a valid answer.
    

**Example 2:**

    
    
    **Input:**  "cbbd"
    **Output:**  "bb"


Similar Questions:
  Shortest Palindrome (shortest-palindrome)
  Palindrome Permutation (palindrome-permutation)
  Palindrome Pairs (palindrome-pairs)
  Longest Palindromic Subsequence (longest-palindromic-subsequence)
  Palindromic Substrings (palindromic-substrings)
"""


class Solution(unittest.TestCase):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return i
                i, j = i + 1, j - 1
            return -1

        val = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if isPalindrome(s[i:j]):
                    if (j - i) > len(val):
                        val = s[i:j]
        return val

    def test(self):
        self.assertEqual(self.longestPalindrome("babad"), "bab")
        self.assertEqual(self.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.longestPalindrome("a"), "a")
        self.assertEqual(self.longestPalindrome("bb"), "bb")
        self.assertEqual(
            self.longestPalindrome(
                "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"),
                "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")


if __name__ == "__main__":
    unittest.main()
