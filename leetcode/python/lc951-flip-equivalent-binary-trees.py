# coding=utf-8
import unittest

"""951. Flip Equivalent Binary Trees
https://leetcode.com/problems/flip-equivalent-binary-trees/description/

For a binary tree T, we can define a flip operation as follows: choose any
node, and swap the left and right child subtrees.

A binary tree X is _flip equivalent_ to a binary tree Y if and only if we can
make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are _flip
equivalent_.   The trees are given by root nodes `root1` and `root2`.



**Example 1:**

    
    
    **Input:** root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
    **Output:** true
    **Explanation:** We flipped at nodes with values 1, 3, and 5.
    ![Flipped Trees Diagram](https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png)
    



**Note:**

  1. Each tree will have at most `100` nodes.
  2. Each value in each tree will be a unique integer in the range `[0, 99]`.


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
