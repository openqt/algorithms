# coding=utf-8
import unittest


class Solution(unittest.TestCase):
    """
    10. Regular Expression Matching

    Implement regular expression matching with support for '.' and '*'.

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.

        The matching should cover the entire input string (not partial).

    The function prototype should be:
        bool isMatch(const char *s, const char *p)

    Some examples:
        isMatch("aa","a") → false
        isMatch("aa","aa") → true
        isMatch("aaa","aa") → false
        isMatch("aa", "a*") → true
        isMatch("aa", ".*") → true
        isMatch("ab", ".*") → true
        isMatch("aab", "c*a*b") → true
    """

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return False

        def _next(i):  # status, value, index
            if i >= len(p):
                return 'X', None, None

            if p[i] == '*':
                return '*', '.', i + 1

            if i == len(p) - 1:
                if p[i] == '.':
                    return '.', None, i + 1
            else:
                if p[i + 1] == '*':
                    return '*', p[i], i + 2

            return None, p[i], i + 1

        status, value, index = _next(0)
        for i in s:
            if status is None:
                if i != value:
                    return False
            elif status == '*':
                if value in ('.', i):
                    continue
            elif status == 'X':
                return False

            status, value, index = _next(index)
        return True

    def test(self):
        self.assertFalse(self.isMatch('aa', 'a'))
        self.assertTrue(self.isMatch('aa', 'aa'))
        self.assertFalse(self.isMatch('aaa', 'aa'))
        self.assertTrue(self.isMatch('aa', 'a*'))
        self.assertTrue(self.isMatch('aa', '*'))
        self.assertTrue(self.isMatch('ab', '*'))
        self.assertTrue(self.isMatch('aab', 'c*a*b'))
        self.assertTrue(self.isMatch('ab', '.*c'))


if __name__ == '__main__':
    unittest.main()
