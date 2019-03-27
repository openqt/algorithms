# coding=utf-8
import unittest

"""500. Keyboard Row
https://leetcode.com/problems/keyboard-row/description/

Given a List of words, return the words that can be typed using letters of
**alphabet** on only one row's of American keyboard like the image below.

  

![American keyboard](/static/images/problemset/keyboard.png)

  

**Example 1:**  

    
    
    **Input:** ["Hello", "Alaska", "Dad", "Peace"]
    **Output:** ["Alaska", "Dad"]
    

**Note:**  

  1. You may use one character in the keyboard more than once.
  2. You may assume the input string will only contain letters of alphabet.


Similar Questions:

"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return [i for i in words if self._one(i) >= 0]

    def _one(self, word: str):
        KEYBOARD = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm"),
        ]
        word = word.lower()
        for n, KEY in enumerate(KEYBOARD):
            if word[0] in KEY: break
        else:
            return -1
        return n if all(c in KEY for c in word) else -1


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])


if __name__ == "__main__":
    unittest.main()
