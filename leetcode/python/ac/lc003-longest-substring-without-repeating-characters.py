# coding=utf-8
import unittest

"""3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string, find the length of the **longest substring** without repeating
characters.

**Examples:**

Given `"abcabcbb"`, the answer is `"abc"`, which the length is 3.

Given `"bbbbb"`, the answer is `"b"`, with the length of 1.

Given `"pwwkew"`, the answer is `"wke"`, with the length of 3. Note that the
answer must be a **substring** , `"pwke"` is a _subsequence_ and not a
substring.


Similar Questions:
  Longest Substring with At Most Two Distinct Characters (longest-substring-with-at-most-two-distinct-characters)
"""


class Solution(unittest.TestCase):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {}
        val, pos = 0, 0
        while pos < len(s):
            if s[pos] in cache:
                pos = cache[s[pos]] + 1
                val = max(val, len(cache))
                cache.clear()
            else:
                cache[s[pos]] = pos
                pos += 1
        val = max(val, len(cache))
        return val

    def test(self):
        self.assertEqual(self.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(self.lengthOfLongestSubstring("c"), 1)


if __name__ == "__main__":
    unittest.main()
