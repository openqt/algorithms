# coding=utf-8
import unittest

"""872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/description/

Consider all the leaves of a binary tree.  From left to right order, the
values of those leaves form a _leaf value sequence._

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9,
8)`.

Two binary trees are considered _leaf-similar_  if their leaf value sequence
is the same.

Return `true` if and only if the two given trees with head nodes `root1` and
`root2` are leaf-similar.



**Note:**

  * Both of the given trees will have between `1` and `100` nodes.


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
