# coding=utf-8
import unittest

"""713. Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/description/

Your are given an array of positive integers `nums`.

Count and print the number of (contiguous) subarrays where the product of all
the elements in the subarray is less than `k`.

**Example 1:**  

    
    
    **Input:** nums = [10, 5, 2, 6], k = 100
    **Output:** 8
    **Explanation:** The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
    Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
    

**Note:**

* `0 < nums.length <= 50000`.
* `0 < nums[i] < 1000`.
* `0 <= k < 10^6`.


Similar Questions:
  Maximum Product Subarray (maximum-product-subarray)
  Maximum Size Subarray Sum Equals k (maximum-size-subarray-sum-equals-k)
  Subarray Sum Equals K (subarray-sum-equals-k)
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
