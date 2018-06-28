# coding=utf-8
import unittest

"""95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer _n_ , generate all structurally unique **BST 's** (binary
search trees) that store values 1 ...  _n_.

**Example:**

    
    
    **Input:** 3
    **Output:**
    [
       [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    **Explanation:**
    The above output corresponds to the 5 unique BST 's shown below:
    
       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


Similar Questions:
  Unique Binary Search Trees (unique-binary-search-trees)
  Different Ways to Add Parentheses (different-ways-to-add-parentheses)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
