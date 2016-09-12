'''
Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''


class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        pos = -1
        for i in range(len(nums)):
            if nums[i] != val:
                pos += 1
                nums[pos] = nums[i]
        return pos + 1


if __name__ == '__main__':
    s = Solution()
    print s.removeElement([1,2,3,3,4], 3) == 3
    print 'PASS'
