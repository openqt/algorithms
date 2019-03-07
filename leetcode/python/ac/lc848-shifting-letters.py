# coding=utf-8
import unittest

"""848. Shifting Letters
https://leetcode.com/problems/shifting-letters/description/

We have a string `S` of lowercase letters, and an integer array `shifts`.

Call the _shift_ of a letter, the next letter in the alphabet, (wrapping
around so that `'z'` becomes `'a'`).

For example, `shift('a') = 'b'`, `shift('t') = 'u'`, and `shift('z') = 'a'`.

Now for each `shifts[i] = x`, we want to shift the first `i+1` letters of `S`,
`x` times.

Return the final string after all such shifts to `S` are applied.

**Example 1:**

    
    
    **Input:** S = "abc", shifts = [3,5,9]
    **Output:** "rpl"
    **Explanation:**
    We start with  "abc".
    After shifting the first 1 letters of S by 3, we have "dbc".
    After shifting the first 2 letters of S by 5, we have "igc".
    After shifting the first 3 letters of S by 9, we have "rpl", the answer.
    

**Note:**

  1. `1 <= S.length = shifts.length <= 20000`
  2. `0 <= shifts[i] <= 10 ^ 9`


Similar Questions:

"""


class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s, n = "", sum(shifts)
        for i in range(len(shifts)):
            if i > 0:
                n -= shifts[i-1]
            s += self._shift(S[i], n)
        return s

    def _shift(self, c, n=1):
        return chr((ord(c) - ord('a') + n) % 26 + ord('a'))


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.shiftingLetters("abc", [3, 5, 9]), "rpl")


if __name__ == "__main__":
    unittest.main()
