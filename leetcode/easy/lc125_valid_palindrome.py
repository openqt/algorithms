# coding=utf-8
"""
125. Valid Palindrome

Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

For example,
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s)-1
        while i < j:
            if not self.is_alpha(s[i]):
                i += 1
            elif not self.is_alpha(s[j]):
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True

    def is_alpha(self, c):
        return 'a' <= c.lower() <= 'z' or '0' <= c <= '9'


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama")
    assert not s.isPalindrome("race a car")
    assert not s.isPalindrome("1a2")
    print 'PASS'
