# coding=utf-8
import unittest

"""345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/description/

Write a function that takes a string as input and reverse only the vowels of a
string.

**Example 1:**  
Given s = "hello", return "holle".

**Example 2:**  
Given s = "leetcode", return "leotcede".

**Note:**  
The vowels does not include the letter "y".


Similar Questions:
  Reverse String (reverse-string)
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        i, j, S = 0, len(s) - 1, list(s)
        while i < j:
            if S[i] in vowels and S[j] in vowels:
                S[i], S[j] = S[j], S[i]
                i += 1
                j -= 1
            if S[i] not in vowels:
                i += 1
            if S[j] not in vowels:
                j -= 1
        return ''.join(S)


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.reverseVowels("aA"), "Aa")
        self.assertEqual(s.reverseVowels("hello"), "holle")
        self.assertEqual(s.reverseVowels("leetcode"), "leotcede")


if __name__ == "__main__":
    unittest.main()
