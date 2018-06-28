# coding=utf-8
import unittest

"""112. Path Sum
https://leetcode.com/problems/path-sum/description/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

**Note:**  A leaf is a node with no children.

**Example:**

Given the below binary tree and `sum = 22`,

    
    
          **5**
         **/** \
        **4**   8
       **/**   / \
      **11**  13  4
     /  **\**      \
    7    **2**      1
    

return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.


Similar Questions:
  Path Sum II (path-sum-ii)
  Binary Tree Maximum Path Sum (binary-tree-maximum-path-sum)
  Sum Root to Leaf Numbers (sum-root-to-leaf-numbers)
  Path Sum III (path-sum-iii)
  Path Sum IV (path-sum-iv)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
