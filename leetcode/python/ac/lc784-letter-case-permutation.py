# coding=utf-8
import unittest

"""784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/description/

Given a string S, we can transform every letter individually to be lowercase
or uppercase to create another string.  Return a list of all possible strings
we could create.

    
    
    **Examples:**
    **Input:** S =  "a1b2"
    **Output:** [ "a1b2", "a1B2", "A1b2", "A1B2"]
    
    **Input:** S =  "3z4"
    **Output:** [ "3z4", "3Z4"]
    
    **Input:** S =  "12345"
    **Output:** [ "12345"]
    

**Note:**

  * `S` will be a string with length at most `12`.
  * `S` will consist only of letters or digits.


Similar Questions:
  Subsets (subsets)
"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.combs = [S]
        self._dfs(S, 0)
        return self.combs

    def _dfs(self, S, n):
        for i in range(n, len(S)):
            c = S[i]
            if 'a' <= c <= 'z':
                S2 = S[:i] + c.upper() + S[i + 1:]
            elif 'A' <= c <= 'Z':
                S2 = S[:i] + c.lower() + S[i + 1:]
            else:
                continue
            self.combs.append(S2)
            self._dfs(S2, i + 1)


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(self.eq(s.letterCasePermutation("a1b2"), ["a1b2", "a1B2", "A1b2", "A1B2"]))
        self.assertTrue(self.eq(s.letterCasePermutation("3z4"), ["3z4", "3Z4"]))
        self.assertTrue(self.eq(s.letterCasePermutation("12345"), ["12345"]))

    def eq(self, a, b):
        return sorted(a) == sorted(b)


if __name__ == "__main__":
    unittest.main()
