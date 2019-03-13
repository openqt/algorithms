# coding=utf-8
import unittest

"""1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

Return the root node of a binary **search** tree that matches the given
`preorder` traversal.

_(Recall that a binary search tree  is a binary tree where for every node, any
descendant of `node.left` has a value `<` `node.val`, and any descendant of
`node.right` has a value `>` `node.val`.  Also recall that a preorder
traversal displays the value of the `node` first, then traverses `node.left`,
then traverses `node.right`.)_



**Example 1:**

    
    
    **Input:** [8,5,1,7,10,12]
    **Output:** [8,5,10,1,7,null,12]
    ![](https://assets.leetcode.com/uploads/2019/03/06/1266.png)
    



**Note:**  

  1. `1 <= preorder.length <= 100`
  2. The values of `preorder` are distinct.


Similar Questions:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        

class T(unittest.TestCase):
    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
