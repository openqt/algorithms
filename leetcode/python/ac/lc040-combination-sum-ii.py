# coding=utf-8
import unittest

"""40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/description/

Given a collection of candidate numbers (`candidates`) and a target number
(`target`), find all unique combinations in `candidates` where the candidate
numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:**

  * All numbers (including `target`) will be positive integers.
  * The solution set must not contain duplicate combinations.

**Example 1:**

    
    
    **Input:** candidates =  [10,1,2,7,6,1,5], target = 8,
    **A solution set is:**
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
    

**Example 2:**

    
    
    **Input:** candidates =  [2,5,2,1,2], target = 5,
    **A solution set is:**
    [
       [1,2,2],
      [5]
    ]


Similar Questions:
  Combination Sum (combination-sum)
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.combs = {}
        self._dfs(sorted(candidates), target, [])
        return list(self.combs.values())

    def _dfs(self, candidates, target, comb):
        for n, i in enumerate(candidates):
            if target > i:
                comb.append(i)
                self._dfs(candidates[n+1:], target - i, comb)
                comb.pop()
            elif target == i:
                val = comb + [i]
                self.combs[str(val)] = val
                return
            else:
                return


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(self.eq(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]))
        self.assertTrue(self.eq(s.combinationSum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]))

    def eq(self, a, b):
        return set([str(i) for i in a]) == set([str(i) for i in b])


if __name__ == "__main__":
    unittest.main()
