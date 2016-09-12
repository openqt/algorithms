# coding=utf-8
"""
053. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = nums[0]
        current = nums[0]
        for i in nums[1:]:
            if current > 0:
                current += i
            else:
                current = i
            largest = max(largest, current)
        return largest


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([-2, 1]) == 1
    assert s.maxSubArray([-1, 1, 2, 1]) == 4
    print 'PASS'
