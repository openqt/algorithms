# coding=utf-8
import unittest

"""145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given a binary tree, return the _postorder_ traversal of its nodes ' values.

**Example:**

    
    
    **Input:**  [1,null,2,3]
       1
        \
         2
        /
       3
    
    **Output:**  [3,2,1]
    

**Follow up:** Recursive solution is trivial, could you do it iteratively?


Similar Questions:
  Binary Tree Inorder Traversal (binary-tree-inorder-traversal)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self._postorder(root, output)
        return output

    def _postorder(self, node, output):
        if node:
            self._postorder(node.left, output)
            self._postorder(node.right, output)
            output.append(node.val)


if __name__ == "__main__":
    unittest.main()
