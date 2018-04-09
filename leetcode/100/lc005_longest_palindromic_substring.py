import unittest


class Solution(unittest.TestCase):
    """5. Longest Palindromic Substring

    Given a string s, find the longest palindromic substring in s. You may
    assume that the maximum length of s is 1000.

    Example:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.

    Example:
        Input: "cbbd"
        Output: "bb"
    """

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def max_s(*args):
            return reduce(lambda a, b: a if len(a) >= len(b) else b, args)

        def get_palindrome(i, even=False):
            j = i + 1 if even else i
            while i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i + 1:j]

        val = s[0]
        for i in range(0, len(s)):
            val = max_s(val, get_palindrome(i, True), get_palindrome(i))
        return val

    def test(self):
        self.assertEqual(self.longestPalindrome('babad'), 'bab')
        self.assertEqual(self.longestPalindrome('cbbd'), 'bb')
        self.assertEqual(self.longestPalindrome('a'), 'a')
        self.assertEqual(self.longestPalindrome('bb'), 'bb')


if __name__ == '__main__':
    unittest.main()
