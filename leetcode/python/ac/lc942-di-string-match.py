# coding=utf-8
import unittest

"""942. DI String Match
https://leetcode.com/problems/di-string-match/description/

Given a string `S` that **only** contains  "I" (increase) or "D" (decrease),
let `N = S.length`.

Return **any** permutation `A` of `[0, 1, ..., N]` such that for all `i = 0,
..., N-1`:

  * If `S[i] == "I"`, then `A[i] < A[i+1]`
  * If `S[i] == "D"`, then `A[i] > A[i+1]`



**Example 1:**

    
    
    **Input:** "IDID"
    **Output:** [0,4,1,3,2]
    

**Example 2:**

    
    
    **Input:** "III"
    **Output:** [0,1,2,3]
    

**Example 3:**

    
    
    **Input:** "DDI"
    **Output:** [3,2,0,1]



**Note:**

  1. `1 <= S.length <= 10000`
  2. `S` only contains characters `"I"` or `"D"`.


Similar Questions:

"""


class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        i, j, A = 0, len(S), []
        for c in S:
            if c == 'I':
                A.append(i)
                i += 1
            else:
                A.append(j)
                j -= 1
        A.append(i)
        return A


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.diStringMatch("IDID"), [0, 4, 1, 3, 2])
        self.assertEqual(s.diStringMatch("III"), [0, 1, 2, 3])
        self.assertEqual(s.diStringMatch("DDI"), [3, 2, 0, 1])


if __name__ == "__main__":
    unittest.main()
