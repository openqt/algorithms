# coding=utf-8
"""
347. Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cache = {}
        for i in nums:
            cache[i] = cache.setdefault(i, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        map(lambda i: freq[cache[i]].append(i), cache)

        ans = []
        map(ans.extend, reversed(freq))
        return ans[:k]


    @print_result
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cache = {}
        for i in nums:
            cache[i] = cache.setdefault(i, 0) + 1
        return sorted(cache.keys(), key=lambda i: cache[i], reverse=True)[:k]


if __name__ == '__main__':
    s = Solution()
    assert set(s.topKFrequent([1,1,1,2,2,3], 2)) == set([1,2])
    assert set(s.topKFrequent([4,1,-1,2,-1,2,3], 2)) == set([-1, 2])
    print 'PASS'
