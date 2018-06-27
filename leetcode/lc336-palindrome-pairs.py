# coding=utf-8
import unittest

"""Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/description/

<p>
    Given a list of <b>unique</b> words, find all pairs of <b><i>distinct</i></b> indices <code>(i, j)</code> in the given list, so that the concatenation of the two words, i.e. <code>words[i] + words[j]</code> is a palindrome.
</p>

<p>
    <b>Example 1:</b><br/>
    Given <code>words</code> = <code>["bat", "tab", "cat"]</code><br/>
    Return <code>[[0, 1], [1, 0]]</code><br/>
    The palindromes are <code>["battab", "tabbat"]</code><br/>
</p>
<p>
    <b>Example 2:</b><br/>
    Given <code>words</code> = <code>["abcd", "dcba", "lls", "s", "sssll"]</code><br/>
    Return <code>[[0, 1], [1, 0], [3, 2], [2, 4]]</code><br/>
    The palindromes are <code>["dcbaabcd", "abcddcba", "slls", "llssssll"]</code><br/>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p>
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
