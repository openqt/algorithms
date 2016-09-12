# coding=utf-8
"""
049. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    For the return value, each inner list's elements must follow the lexicographic order.
    All inputs will be in lower-case.
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        cache = {}
        for i in strs:
            key = ''.join(sorted(i))
            cache.setdefault(key, []).append(i)
        return [sorted(i) for i in cache.values()]

if __name__ == '__main__':
    s = Solution()
    assert s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["nat", "tan"],
                                                                           ["bat"],
                                                                           ["ate", "eat", "tea"],
                                                                           ]
    print 'PASS'
