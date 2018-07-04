# coding=utf-8
import unittest

"""653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given a Binary Search Tree and a target number, return true if there exist two
elements in the BST such that their sum is equal to the given target.

**Example 1:**  

    
    
    **Input:** 
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Target = 9
    
    **Output:** True
    

**Example 2:**  

    
    
    **Input:** 
        5
       / \
      3   6
     / \   \
    2   4   7
    
    Target = 28
    
    **Output:** False


Similar Questions:
  Two Sum (two-sum)
  Two Sum II - Input array is sorted (two-sum-ii-input-array-is-sorted)
  Two Sum III - Data structure design (two-sum-iii-data-structure-design)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(unittest.TestCase):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        def preorder(root):
            if root:
                vals.append(root.val)
                preorder(root.left)
                preorder(root.right)

        vals = []
        preorder(root)
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                if vals[i] + vals[j] == k:
                    return True
        return False

    def test(self):
        from tree import BinaryTree
        self.assertTrue(self.findTarget(BinaryTree([5, 3, 6, 2, 4, '#', 7]).root, 9))
        self.assertFalse(self.findTarget(BinaryTree([5, 3, 6, 2, 4, '#', 7]).root, 28))


if __name__ == "__main__":
    unittest.main()
