# coding=utf-8
import unittest

"""344. Reverse String
https://leetcode.com/problems/reverse-string/description/

Write a function that takes a string as input and returns the string reversed.

**Example:**  
Given s = "hello", return "olleh".


Similar Questions:
  Reverse Vowels of a String (reverse-vowels-of-a-string)
  Reverse String II (reverse-string-ii)
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        l = ["h", "e", "l", "l", "o"]
        s.reverseString(l)
        self.assertEqual(l, ["o", "l", "l", "e", "h"])

        l = ["H", "a", "n", "n", "a", "h"]
        s.reverseString(l)
        self.assertEqual(l, ["h", "a", "n", "n", "a", "H"])


if __name__ == "__main__":
    unittest.main()
