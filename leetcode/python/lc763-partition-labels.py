# coding=utf-8
import unittest

"""763. Partition Labels
https://leetcode.com/problems/partition-labels/description/

A string `S` of lowercase letters is given. We want to partition this string
into as many parts as possible so that each letter appears in at most one
part, and return a list of integers representing the size of these parts.

**Example 1:**  

    
    
    **Input:** S = "ababcbacadefegdehijhklij"
    **Output:** [9,7,8]
    **Explanation:**
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
    

**Note:**  

  1. `S` will have length in range `[1, 500]`.
  2. `S` will consist of lowercase letters (`'a'` to `'z'`) only.


Similar Questions:
  Merge Intervals (merge-intervals)
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
