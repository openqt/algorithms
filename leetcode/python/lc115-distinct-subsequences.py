# coding=utf-8
import unittest

"""115. Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/description/

Given a string **S** and a string **T** , count the number of distinct
subsequences of **S** which equals **T**.

A subsequence of a string is a new string which is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (ie, `"ACE"` is a subsequence
of `"ABCDE"` while `"AEC"` is not).

**Example 1:**

    
    
    **Input:** S = "rabbbit", T = "rabbit"
    **Output:**  3
    **Explanation:**
    As shown below, there are 3 ways you can generate  "rabbit" from S.
    (The caret symbol ^ means the chosen letters)
    
    rabbbit
    ^^^^ ^^
    rabbbit
    ^^ ^^^^
    rabbbit
    ^^^ ^^^
    

**Example 2:**

    
    
    **Input:** S = "babgbag", T = "bag"
    **Output:**  5
    **Explanation:**
    As shown below, there are 5 ways you can generate  "bag" from S.
    (The caret symbol ^ means the chosen letters)
    
    babgbag
    ^^ ^
    babgbag
    ^^    ^
    babgbag
    ^    ^^
    babgbag
      ^  ^^
    babgbag
        ^^^


Similar Questions:

"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()