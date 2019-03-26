# coding=utf-8
import unittest

"""908. Smallest Range I
https://leetcode.com/problems/smallest-range-i/description/

Given an array `A` of integers, for each integer `A[i]` we may choose any `x`
with `-K <= x <= K`, and add `x` to `A[i]`.

After this process, we have some array `B`.

Return the smallest possible difference between the maximum value of `B` and
the minimum value of `B`.



**Example 1:**

    
    
    **Input:** A = [1], K = 0
    **Output:** 0
    **Explanation** : B = [1]
    

**Example 2:**

    
    
    **Input:** A = [0,10], K = 2
    **Output:** 6
    **Explanation** : B = [2,8]
    

**Example 3:**

    
    
    **Input:** A = [1,3,6], K = 3
    **Output:** 0
    **Explanation** : B = [3,3,3] or B = [4,4,4]
    



**Note:**

  1. `1 <= A.length <= 10000`
  2. `0 <= A[i] <= 10000`
  3. `0 <= K <= 10000`


Similar Questions:

"""


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        val = max(A) - min(A) - 2 * K
        return val if val > 0 else 0


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.smallestRangeI([1], 0), 0)
        self.assertEqual(s.smallestRangeI([0, 10], 2), 6)
        self.assertEqual(s.smallestRangeI([1, 3, 6], 3), 0)


if __name__ == "__main__":
    unittest.main()
