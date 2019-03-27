# coding=utf-8
import unittest

"""438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given a string **s** and a **non-empty** string **p** , find all the start
indices of **p** 's anagrams in **s**.

Strings consists of lowercase English letters only and the length of both
strings **s** and **p** will not be larger than 20,100.

The order of output does not matter.

**Example 1:**

    
    
    **Input:**
    s: "cbaebabacd" p: "abc"
    
    **Output:**
    [0, 6]
    
    **Explanation:**
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    

**Example 2:**

    
    
    **Input:**
    s: "abab" p: "ab"
    
    **Output:**
    [0, 1, 2]
    
    **Explanation:**
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".


Similar Questions:
  Valid Anagram (valid-anagram)
  Permutation in String (permutation-in-string)
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p): return []

        n, hp, ht = 0, {}, {}
        while n < len(p):
            hp[p[n]] = hp.setdefault(p[n], 0) + 1
            ht[s[n]] = ht.setdefault(s[n], 0) + 1
            n += 1
        vals = [0] if hp == ht else []

        while n < len(s):
            a, b = s[n - len(p)], s[n]
            if ht[a] <= 1:
                del ht[a]
            else:
                ht[a] -= 1
            ht[b] = ht.setdefault(b, 0) + 1

            if hp == ht:
                vals.append(n - len(p) + 1)
            n += 1
        return vals


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.findAnagrams("", 'a'), [])
        self.assertEqual(s.findAnagrams("af", 'be'), [])
        self.assertEqual(s.findAnagrams("cbaebabacd", 'abc'), [0, 6])
        self.assertEqual(s.findAnagrams("abab", 'ab'), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
