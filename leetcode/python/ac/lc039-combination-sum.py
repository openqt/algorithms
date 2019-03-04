# coding=utf-8
import unittest

"""39. Combination Sum
https://leetcode.com/problems/combination-sum/description/

Given a **set** of candidate numbers (`candidates`) **(without duplicates)**
and a target number (`target`), find all unique combinations in `candidates`
where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number
of times.

**Note:**

  * All numbers (including `target`) will be positive integers.
  * The solution set must not contain duplicate combinations.

**Example 1:**

    
    
    **Input:** candidates = [2,3,6,7], target = 7,
    **A solution set is:**
    [
      [7],
      [2,2,3]
    ]
    

**Example 2:**

    
    
    **Input:** candidates = [2,3,5], target = 8,
    **A solution set is:**
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]


Similar Questions:
  Letter Combinations of a Phone Number (letter-combinations-of-a-phone-number)
  Combination Sum II (combination-sum-ii)
  Combinations (combinations)
  Combination Sum III (combination-sum-iii)
  Factor Combinations (factor-combinations)
  Combination Sum IV (combination-sum-iv)
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.combs = {}
        self._dfs(sorted(candidates), target, [])
        # print(self.combs)
        return list(self.combs.values())

    def _dfs(self, candidates, target, comb):
        for i in candidates:
            if target > i:
                comb.append(i)
                self._dfs(candidates, target - i, comb)
                comb.pop()
            elif target == i:
                val = sorted(comb + [i])
                self.combs[str(val)] = val
                return
            else:
                return


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        self.assertEqual(s.combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
        self.assertEqual(s.combinationSum([8, 7, 4, 3], 11), [[3, 4, 4], [3, 8], [4, 7]])


if __name__ == "__main__":
    unittest.main()
