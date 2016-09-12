'''
Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums) * (len(nums) + 1) / 2
        current = sum(nums)
        return total - current


if __name__ == '__main__':
    s = Solution()
    print s.missingNumber([0,1,2,3,4])
    print 'PASS'
