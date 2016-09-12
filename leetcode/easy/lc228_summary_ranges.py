# -*- encoding: utf-8 -*-
'''
Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) <= 0: return []

        ret = []
        a = b = nums[0]
        for i in nums[1:]:
            if i - b == 1:
                b = i
            else:
                ret.append(self._range(a, b))
                a = b = i
        ret.append(self._range(a, b))
        return ret

    def _range(self, a, b):
        if a == b:
            return str(b)
        else:
            return '{}->{}'.format(a, b)


if __name__ == '__main__':
    s = Solution()
    print s.summaryRanges([0,1,2,4,5,7])
    print s.summaryRanges([7])
    print 'PASS'
