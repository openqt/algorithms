# coding=utf-8
"""
214. Shortest Palindrome

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

    Given "aacecaaa", return "aaacecaaa".

    Given "abcd", return "dcbabcd".
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


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
    assert s.shortestPalindrome('aacecaaa') == 'aaacecaaa'
    assert s.shortestPalindrome('abcd') == 'dcbabcd'
    print 'PASS'
