# coding=utf-8
import unittest

"""106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

Given inorder and postorder traversal of a tree, construct the binary tree.

**Note:**  
You may assume that duplicates do not exist in the tree.

For example, given

    
    
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]

Return the following binary tree:

    
    
        3
       / \
      9  20
        /  \
       15   7


Similar Questions:
  Construct Binary Tree from Preorder and Inorder Traversal (construct-binary-tree-from-preorder-and-inorder-traversal)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
