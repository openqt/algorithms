# coding=utf-8
import unittest

"""557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

**Example 1:**  

    
    
    **Input:** "Let's take LeetCode contest"
    **Output:** "s'teL ekat edoCteeL tsetnoc"
    

**Note:** In the string, each word is separated by single space and there will
not be any extra space in the string.


Similar Questions:
  Reverse String II (reverse-string-ii)
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, t = 0, ''
        for j in range(len(s)):
            if s[j] == ' ':
                t += ''.join(reversed(s[i:j])) + ' '
                i = j + 1
            j += 1
        t += ''.join(reversed(s[i:]))
        return t


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")


if __name__ == "__main__":
    unittest.main()
