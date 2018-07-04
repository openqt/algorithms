# coding=utf-8
import unittest
import os

"""14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

    
    
    **Input:** ["flower","flow","flight"]
    **Output:**  "fl"
    

**Example 2:**

    
    
    **Input:** ["dog","racecar","car"]
    **Output:**  ""
    **Explanation:** There is no common prefix among the input strings.
    

**Note:**

All given inputs are in lowercase letters `a-z`.


Similar Questions:

"""


class Solution(unittest.TestCase):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in range(min([len(s) for s in strs])):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

    def test(self):
        self.assertEqual(os.path.commonprefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(self.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(self.longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(self.longestCommonPrefix([]), "")
        self.assertEqual(self.longestCommonPrefix(["aca", "cba"]), "")


if __name__ == "__main__":
    unittest.main()
