# coding=utf-8
import unittest

"""90. Subsets II
https://leetcode.com/problems/subsets-ii/description/

Given a collection of integers that might contain duplicates, **_nums_** ,
return all possible subsets (the power set).

**Note:** The solution set must not contain duplicate subsets.

**Example:**

    
    
    **Input:** [1,2,2]
    **Output:**
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]


Similar Questions:
  Subsets (subsets)
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combs = {str([]): []}
        for n in nums:
            vals = [sorted(i + [n]) for i in combs.values()] + [[n]]
            combs.update({str(i): i for i in vals})
        return list(combs.values())


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(self.eq(s.subsetsWithDup([1, 2, 2]), [[2], [1], [1, 2, 2], [2, 2], [1, 2], []]))
        self.assertTrue(self.eq(s.subsetsWithDup([4,4,4,1,4]), [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]))

    def eq(self, a, b):
        return set([str(i) for i in a]) == set([str(i) for i in b])


if __name__ == "__main__":
    unittest.main()
