# coding=utf-8
import unittest

"""658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/description/

Given a sorted array, two integers `k` and `x`, find the `k` closest elements
to `x` in the array. The result should also be sorted in ascending order. If
there is a tie, the smaller elements are always preferred.

**Example 1:**  

    
    
    **Input:** [1,2,3,4,5], k=4, x=3
    **Output:** [1,2,3,4]
    

**Example 2:**  

    
    
    **Input:** [1,2,3,4,5], k=4, x=-1
    **Output:** [1,2,3,4]
    

**Note:**  

  1. The value k is positive and will always be smaller than the length of the sorted array.
  2. Length of the given array is positive and will not exceed 104
  3. Absolute value of elements in the array and x will not exceed 104

* * *

**UPDATE (2017/9/19):**  
The _arr_ parameter had been changed to an **array of integers** (instead of a
list of integers). **_Please reload the code definition to get the latest
changes_**.


Similar Questions:
  Guess Number Higher or Lower (guess-number-higher-or-lower)
  Guess Number Higher or Lower II (guess-number-higher-or-lower-ii)
  Find K-th Smallest Pair Distance (find-k-th-smallest-pair-distance)
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        r = self._binary_find(arr, x)  # 这是比k大的位置所以是右边界
        l = r - 1
        val = []
        while len(val) < k:
            if l < 0:
                val.append(arr[r])
                r += 1
            elif r >= len(arr):
                val.append(arr[l])
                l -= 1
            else:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    val.append(arr[l])
                    l -= 1
                else:
                    val.append(arr[r])
                    r += 1
        return sorted(val)

    def _binary_find(self, arr, k):
        """返回k应该插入的位置"""
        l, r = 0, len(arr)
        while l < r:
            m = (r + l) // 2
            if arr[m] < k:
                l = m + 1
            elif arr[m] > k:
                r = m
            else:
                return m
        return l


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.findClosestElements([1], 1, 1), [1])
        self.assertEqual(s.findClosestElements([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4])
        self.assertEqual(s.findClosestElements([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4])

        self.assertEqual(s.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5), [3, 3, 4])


if __name__ == "__main__":
    unittest.main()
