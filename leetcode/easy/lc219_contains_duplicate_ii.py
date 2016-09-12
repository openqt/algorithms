'''
Contains Duplicate II

Given an array of integers and an integer k,
find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        m = {}
        for n, i in enumerate(nums):
            if i not in m:
                m[i] = n
            else:
                if n - m[i] <= k:
                    return True
                else:
                    m[i] = n
        return False


if __name__ == '__main__':
    s = Solution()
    print s.containsNearbyDuplicate([], 0)
    print s.containsNearbyDuplicate([1,6,3,7,3,7,9,5,4,5,7], 3)
    print 'PASS'
