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

        def maxPalindrome(s, l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l + 1:r]

        val = ""
        for i in range(len(s)):
            val = max(val, maxPalindrome(s, i, i), maxPalindrome(s, i, i + 1), key=len)

        return val

    def test(self):
        self.assertEqual(self.longestPalindrome("babad"), "bab")
        self.assertEqual(self.longestPalindrome("cbbd"), "bb")
        self.assertEqual(self.longestPalindrome("a"), "a")
        self.assertEqual(self.longestPalindrome("bb"), "bb")
        self.assertEqual(self.longestPalindrome(
            "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"),
            "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")


if __name__ == "__main__":
    unittest.main()
