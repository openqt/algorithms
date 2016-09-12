# -*- encoding: utf-8 -*-
'''
Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
'''


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        k %= len(nums)
        l = len(nums) - k

        n = nums[l:]
        nums[k:] = nums[:l]
        nums[:k] = n


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    s.rotate(nums, 3)
    print nums == [5,6,7,1,2,3,4]
    print 'PASS'
