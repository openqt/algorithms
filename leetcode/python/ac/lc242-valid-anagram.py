# coding=utf-8
import unittest

"""242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

Given two strings _s_ and _t  _, write a function to determine if _t_ is an
anagram of _s_.

**Example 1:**

    
    
    **Input:** _s_ =  "anagram", _t_ =  "nagaram"
    **Output:** true
    

**Example 2:**

    
    
    **Input:** _s_ =  "rat", _t_ =  "car"
    **Output:** false
    

**Note:**  
You may assume the string contains only lowercase alphabets.

**Follow up:**  
What if the inputs contain unicode characters? How would you adapt your
solution to such case?


Similar Questions:
  Group Anagrams (group-anagrams)
  Palindrome Permutation (palindrome-permutation)
  Find All Anagrams in a String (find-all-anagrams-in-a-string)
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        

class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.isAnagram("anagram", "nagaram"))
        self.assertFalse(s.isAnagram("rat", "car"))


if __name__ == "__main__":
    unittest.main()
