# coding=utf-8
import unittest

"""139. Word Break
https://leetcode.com/problems/word-break/description/

Given a **non-empty** string _s_ and a dictionary _wordDict_ containing a list
of **non-empty** words, determine if _s_ can be segmented into a space-
separated sequence of one or more dictionary words.

**Note:**

  * The same word in the dictionary may be reused multiple times in the segmentation.
  * You may assume the dictionary does not contain duplicate words.

**Example 1:**

    
    
    **Input:** s =  "leetcode", wordDict = ["leet", "code"]
    **Output:** true
    **Explanation:** Return true because "leetcode" can be segmented as "leet code".
    

**Example 2:**

    
    
    **Input:** s =  "applepenapple", wordDict = ["apple", "pen"]
    **Output:** true
    **Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.
    

**Example 3:**

    
    
    **Input:** s =  "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    **Output:** false


Similar Questions:
  Word Break II (word-break-ii)
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        

class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.wordBreak("leetcode", ["leet", "code"]))
        self.assertTrue(s.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertFalse(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))


if __name__ == "__main__":
    unittest.main()
