# coding=utf-8
import unittest

"""30. Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

<p>You are given a string, <strong>s</strong>, and a list of words, <strong>words</strong>, that are all of the same length. Find all starting indices of substring(s) in <strong>s</strong> that is a concatenation of each word in <strong>words</strong> exactly once and without any intervening characters.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>Output:</strong> <code>[0,9]</code>
<strong>Explanation:</strong> Substrings starting at index 0 and 9 are &quot;barfoor&quot; and &quot;foobar&quot; respectively.
The output order does not matter, returning [9,0] is fine too.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;wordgoodstudentgoodword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;student&quot;]
<strong>Output:</strong> <code>[]</code>
</pre>

Similar Questions:
  Minimum Window Substring (minimum-window-substring)
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
