# coding=utf-8
import unittest

"""99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/description/

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

**Example 1:**

    
    
    **Input:** [1,3,null,null,2]
    
        1
      /
     3
      \
       2
    
    **Output:** [3,1,null,null,2]
    
        3
      /
     1
      \
       2
    

**Example 2:**

    
    
    **Input:** [3,1,4,null,null,2]
    
      3
     / \
    1   4
        /
      2
    
    **Output:** [2,1,4,null,null,3]
    
      2
     / \
    1   4
        /
      3
    

**Follow up:**

  * A solution using O( _n_ ) space is pretty straight forward.
  * Could you devise a constant space solution?


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
