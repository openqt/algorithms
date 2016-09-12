'''
Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''


class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        pos = m + n - 1; i = m - 1; j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[pos] = nums1[i]
                i -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
            pos -= 1
        while j >= 0:
            nums1[pos] = nums2[j]
            pos -= 1; j -= 1


if __name__ == '__main__':
    s = Solution()
    nums1 = [3,5,7,0,0,0]
    s.merge(nums1, 3, [2,4,6], 3)
    print nums1
    print 'PASS'
