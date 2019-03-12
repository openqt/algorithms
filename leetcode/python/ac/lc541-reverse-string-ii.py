# coding=utf-8
import unittest

"""541. Reverse String II
https://leetcode.com/problems/reverse-string-ii/description/

Given a string and an integer k, you need to reverse the first k characters
for every 2k characters counting from the start of the string. If there are
less than k characters left, reverse all of them. If there are less than 2k
but greater than or equal to k characters, then reverse the first k characters
and left the other as original.

**Example:**  

    
    
    **Input:** s = "abcdefg", k = 2
    **Output:** "bacdfeg"
    

**Restrictions:** **

  1. The string consists of lower English letters only.
  2. Length of the given string and k will in the range [1, 10000]


Similar Questions:
  Reverse String (reverse-string)
  Reverse Words in a String III (reverse-words-in-a-string-iii)
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = list(s)
        n = 0
        while n + 2 * k < len(l):
            self._reverse(l, n, n + k)
            n += 2 * k
        self._reverse(l, n, min(len(l), n + k))
        return ''.join(l)

    def _reverse(self, s, l, r):  # reverse in place
        r -= 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.reverseStr("a", 2), "a")
        self.assertEqual(s.reverseStr("abcdefg", 2), "bacdfeg")


if __name__ == "__main__":
    unittest.main()
