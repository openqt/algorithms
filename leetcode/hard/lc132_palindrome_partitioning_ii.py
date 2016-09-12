# coding=utf-8
"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if self.is_palindrome(s[:i]) and self.is_palindrome(s[i:]):
                pass

    def dfs(self, a, deep):
        if self.is_palindrome(a) and self.is_palindrome(b):
            return True

        for i in range(len(a)):
            left = self.dfs(a[:i], a[i:], deep+1)



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
    assert s.minCut('aab') == 1
    print 'PASS'
