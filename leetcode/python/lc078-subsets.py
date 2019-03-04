# coding=utf-8
import unittest

"""78. Subsets
https://leetcode.com/problems/subsets/description/

Given a set of **distinct** integers, _nums_ , return all possible subsets
(the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

    
    
    **Input:** nums = [1,2,3]
    **Output:**
    [
      [3],
       [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]


Similar Questions:
  Subsets II (subsets-ii)
  Generalized Abbreviation (generalized-abbreviation)
  Letter Case Permutation (letter-case-permutation)
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """



class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(self.eq(s.subsets([1, 2, 2]), [[2], [1], [1, 2, 2], [2, 2], [1, 2], []]))

    def eq(self, a, b):
        return set([str(i) for i in a]) == set([str(i) for i in b])


if __name__ == "__main__":
    unittest.main()
