'''
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums: return 0

        pos = 0
        prev = nums[pos]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                pos += 1
                nums[pos] = nums[i]
                prev = nums[i]
        return pos+1


if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicates([1,1,2]) == 2
    print s.removeDuplicates([1,3,2]) == 3
    print s.removeDuplicates([1,2,2]) == 2
    print 'PASS'
