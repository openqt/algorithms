# coding=utf-8
import unittest

"""744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

Given a list of sorted characters `letters` containing only lowercase letters,
and given a target letter `target`, find the smallest element in the list that
is larger than the given target.

Letters also wrap around. For example, if the target is `target = 'z'` and
`letters = ['a', 'b']`, the answer is `'a'`.

**Examples:**  

    
    
    **Input:**
    letters = ["c", "f", "j"]
    target = "a"
    **Output:** "c"
    
    **Input:**
    letters = ["c", "f", "j"]
    target = "c"
    **Output:** "f"
    
    **Input:**
    letters = ["c", "f", "j"]
    target = "d"
    **Output:** "f"
    
    **Input:**
    letters = ["c", "f", "j"]
    target = "g"
    **Output:** "j"
    
    **Input:**
    letters = ["c", "f", "j"]
    target = "j"
    **Output:** "c"
    
    **Input:**
    letters = ["c", "f", "j"]
    target = "k"
    **Output:** "c"
    

**Note:**  

  1. `letters` has a length in range `[2, 10000]`.
  2. `letters` consists of lowercase letters, and contains at least 2 unique letters.
  3. `target` is a lowercase letter.


Similar Questions:

"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]), 16)


if __name__ == "__main__":
    unittest.main()
