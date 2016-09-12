# coding=utf-8
"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.cache = []
        self.dfs(s, [])
        return self.cache

    def dfs(self, s, l):
        if len(s) == 0:
            self.cache.append([i for i in l])  # 复制list
            return

        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                l.append(s[:i+1])
                self.dfs(s[i+1:], l)
                l.pop()

    def is_palindrome(self, s):
        i, j = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.partition('aab')) == sorted([["aa", "b"], ["a", "a", "b"]])
    print 'PASS'
