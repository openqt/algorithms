# coding=utf-8
import unittest

"""543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/description/

Given a binary tree, you need to compute the length of the diameter of the
tree. The diameter of a binary tree is the length of the **longest** path
between any two nodes in a tree. This path may or may not pass through the
root.

**Example:**  
Given a binary tree  

    
    
              1
             / \
            2   3
           / \     
          4   5    
    

Return **3** , which is the length of the path [4,2,1,3] or [5,2,1,3].

**Note:** The length of path between two nodes is represented by the number of
edges between them.


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return max(self._depth(root.left) + self._depth(root.right),
                       self.diameterOfBinaryTree(root.left),
                       self.diameterOfBinaryTree(root.right))
        return 0

    def _depth(self, node):
        if node:
            return max(self._depth(node.left), self._depth(node.right)) + 1
        return 0


import tree
class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.diameterOfBinaryTree(None), 0)
        self.assertEqual(s.diameterOfBinaryTree(tree.BinaryTree("12345").root), 3)
        self.assertEqual(s.diameterOfBinaryTree(tree.BinaryTree(
            [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5,
             None, 9, None, None, -1, -4, None, None, None, -2]).root), 8)


if __name__ == "__main__":
    unittest.main()
