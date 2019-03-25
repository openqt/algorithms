# coding=utf-8
import unittest

"""1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/description/

Given an array `A` of strings made only from lowercase letters, return a list
of all characters that show up in all strings within the list **(including
duplicates)**.   For example, if a character occurs 3 times in all strings but
not 4 times, you need to include that character three times in the final
answer.

You may return the answer in any order.



**Example 1:**

    
    
    **Input:** ["bella","label","roller"]
    **Output:** ["e","l","l"]
    

**Example 2:**

    
    
    **Input:** ["cool","lock","cook"]
    **Output:** ["c","o"]
    



**Note:**

  1. `1 <= A.length <= 100`
  2. `1 <= A[i].length <= 100`
  3. `A[i][j]` is a lowercase letter


Similar Questions:
  Intersection of Two Arrays II (intersection-of-two-arrays-ii)
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        data = self._min(self._dict(A[0]), self._dict(A[0]))
        for s in A[1:]:
            data = self._min(data, self._dict(s))

        L = []
        for i, j in data.items():
            L.extend(list(i * j))
        return L

    def _dict(self, s):
        d = {}
        for c in s:
            d[c] = d.setdefault(c, 0) + 1
        return d

    def _min(self, a, b):
        c = {}
        for i in a:
            if i in b:
                c[i] = min(a[i], b[i])
        return c


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.commonChars(["bella", "label", "roller"]), ["e", "l", "l"])
        self.assertEqual(s.commonChars(["cool", "lock", "cook"]), ["c", "o"])


if __name__ == "__main__":
    unittest.main()
