# -*- encoding: utf-8 -*-
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.

Hint:

    How many majority elements could it possibly have?
    Do you have a better hint? Suggest it!
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        size = len(nums)
        if size <= 1: return nums

        n1, c1 = None, 0
        n2, c2 = None, 0
        for i in nums:
            # print n1, c1, n2, c2
            if i == n1: c1 += 1
            elif i == n2: c2 += 1
            else:
                if c1 <= 0:
                    n1 = i; c1 = 1
                elif c2 <= 0:
                    n2 = i; c2 = 1
                else:
                    c1 -= 1; c2 -= 1

        val = []
        c1 = c2 = 0
        for i in nums:
            if i == n1: c1 += 1
            elif i == n2: c2 += 1
        if n1 is not None and c1 > size/3: val.append(n1)
        if n2 is not None and c2 > size/3: val.append(n2)
        return val


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement([1]) == [1]
    print s.majorityElement([1, 2]) == [1, 2]
    print s.majorityElement([2, 2]) == [2]
    print s.majorityElement([3, 2, 3]) == [3]
    print s.majorityElement([0,0,0]) == [0]
    print s.majorityElement([2,2,1,3]) == [2]
    print s.majorityElement([1,2,3,4,5,5,5,0,5,5,6]) == [5]
    print 'PASS'
