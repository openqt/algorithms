# coding=utf-8
import unittest

"""965. Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/description/

A binary tree is _univalued_ if every node in the tree has the same value.

Return `true` if and only if the given tree is univalued.



**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_1.png)

    
    
    **Input:** [1,1,1,1,1,null,1]
    **Output:** true
    

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/28/unival_bst_2.png)

    
    
    **Input:** [2,2,2,5,2]
    **Output:** false
    



**Note:**

  1. The number of nodes in the given tree will be in the range `[1, 100]`.
  2. Each node's value will be an integer in the range `[0, 99]`.


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if root.left and root.left.val != root.val: return False
        if root.right and root.right.val != root.val: return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        

if __name__ == "__main__":
    unittest.main()
