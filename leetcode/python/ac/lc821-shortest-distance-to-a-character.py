# coding=utf-8
import unittest

"""821. Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/description/

Given a string `S` and a character `C`, return an array of integers
representing the shortest distance from the character `C` in the string.

**Example 1:**

    
    
    **Input:** S =  "loveleetcode", C = 'e'
    **Output:** [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    



**Note:**

  1. `S` string length is in `[1, 10000].`
  2. `C` is a single character, and guaranteed to be in string `S`.
  3. All letters in `S` and `C` are lowercase.


Similar Questions:

"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        val = [0] * len(S)
        v = len(S)
        for n, c in enumerate(S):
            v = 0 if c == C else v + 1
            val[n] = v

        v = len(S)
        for i in range(n, -1, -1):
            v = 0 if S[i] == C else v + 1
            val[i] = min(val[i], v)

        return val


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.shortestToChar("aaab", 'b'), [3,2,1,0])
        self.assertEqual(s.shortestToChar("loveleetcode", 'e'),
                         [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()
