import unittest


class Solution(unittest.TestCase):
    """3. Longest Substring Without Repeating Characters

    Given a string, find the length of the longest substring without repeating
    characters.

    Examples:
        Given "abcabcbb", the answer is "abc", which the length is 3.

        Given "bbbbb", the answer is "b", with the length of 1.

        Given "pwwkew", the answer is "wke", with the length of 3. Note that
        the answer must be a substring, "pwke" is a subsequence and not a
        substring.
    """

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def max_s(s1, s2):
            return s1 if len(s1) > len(s2) else s2

        longest = subs = ''
        for i in s:
            pos = subs.find(i)
            if pos > -1:
                longest = max_s(longest, subs)
                subs = subs[pos + 1:] + i
            else:
                subs += i

        longest = max_s(longest, subs)
        return len(longest)

    def test(self):
        self.assertEqual(self.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(self.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(self.lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(self.lengthOfLongestSubstring('c'), 1)
        self.assertEqual(self.lengthOfLongestSubstring('dvdf'), 3)


if __name__ == '__main__':
    unittest.main()
