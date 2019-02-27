# coding=utf-8
import unittest

"""410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/description/

Given an array which consists of non-negative integers and an integer _m_ ,
you can split the array into _m_ non-empty continuous subarrays. Write an
algorithm to minimize the largest sum among these _m_ subarrays.

**Note:**  
If _n_ is the length of array, assume the following constraints are satisfied:

  * 1 ≤ _n_ ≤ 1000
  * 1 ≤ _m_ ≤ min(50, _n_ )

**Examples:**

    
    
    Input:
    **nums** = [7,2,5,10,8]
    **m** = 2
    
    Output:
    18
    
    Explanation:
    There are four ways to split **nums** into two subarrays.
    The best way is to split it into **[7,2,5]** and **[10,8]** ,
    where the largest sum among the two subarrays is only 18.


Similar Questions:

"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l+r)//2
            if self._min_group(nums, mid) > m:
                l = mid + 1
            else:
                r = mid
        return l

    def _min_group(self, nums, m):
        count, val = 1, 0
        for n in nums:
            val += n
            if val > m:
                val = n
                count += 1
        return count


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.splitArray([7, 2, 5, 10, 8], 2), 18)
        self.assertEqual(s.splitArray([1, 2, 3, 4, 5], 3), 6)


if __name__ == "__main__":
    unittest.main()
