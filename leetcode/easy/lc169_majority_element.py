# -*- encoding: utf-8 -*-
'''
Majority Element

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        c = None; n = 0
        for i in nums:
            if c == i:
                n += 1
            else:
                n -= 1
                if n <= 0:
                    n = 1
                    c = i
        return c


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([2,3,4,5,5,6,6,6,6,6,7])
    print s.majorityElement([3,3,4])
    print 'PASS'
