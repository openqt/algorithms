# coding=utf-8
import unittest

"""524. Longest Word in Dictionary through Deleting
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

Given a string and a string dictionary, find the longest string in the
dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the
smallest lexicographical order. If there is no possible result, return the
empty string.

**Example 1:**  

    
    
    **Input:**
    s = "abpcplea", d = ["ale","apple","monkey","plea"]
    
    **Output:** 
    "apple"
    

**Example 2:**  

    
    
    **Input:**
    s = "abpcplea", d = ["a","b","c"]
    
    **Output:** 
    "a"
    

**Note:**  

  1. All the strings in the input will only contain lower-case letters.
  2. The size of the dictionary won't exceed 1,000.
  3. The length of all the strings in the input won't exceed 1,000.


Similar Questions:
  Longest Word in Dictionary (longest-word-in-dictionary)
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
