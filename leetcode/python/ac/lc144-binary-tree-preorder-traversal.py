# coding=utf-8
import unittest

"""144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given a binary tree, return the _preorder_ traversal of its nodes ' values.

**Example:**

    
    
    **Input:**  [1,null,2,3]
       1
        \
         2
        /
       3
    
    **Output:**  [1,2,3]
    

**Follow up:** Recursive solution is trivial, could you do it iteratively?


Similar Questions:
  Binary Tree Inorder Traversal (binary-tree-inorder-traversal)
  Verify Preorder Sequence in Binary Search Tree (verify-preorder-sequence-in-binary-search-tree)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self._preorder(root, output)
        return output
        

    def _preorder(self, node, output):
        if node:
            output.append(node.val)
            self._preorder(node.left, output)
            self._preorder(node.right, output)


if __name__ == "__main__":
    unittest.main()
