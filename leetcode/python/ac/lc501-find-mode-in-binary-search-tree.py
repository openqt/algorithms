# coding=utf-8
import unittest

"""501. Find Mode in Binary Search Tree
https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

Given a binary search tree (BST) with duplicates, find all the
[mode(s)](https://en.wikipedia.org/wiki/Mode_\(statistics\)) (the most
frequently occurred element) in the given BST.

Assume a BST is defined as follows:

  * The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
  * The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
  * Both the left and right subtrees must also be binary search trees.

For example:  
Given BST `[1,null,2,2]`,  

    
    
       1
        \
         2
        /
       2
    

return `[2]`.

**Note:** If a tree has more than one mode, you can return them in any order.

**Follow up:** Could you do that without using any extra space? (Assume that
the implicit stack space incurred due to recursion does not count).


Similar Questions:
  Validate Binary Search Tree (validate-binary-search-tree)
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.mem = {}
        self._preorder(root)
        if not self.mem: return []
        n = max(self.mem.values())
        return [i for i in self.mem if self.mem[i] == n]

    def _preorder(self, node):
        if node:
            self.mem[node.val] = self.mem.setdefault(node.val, 0) + 1
            self._preorder(node.left)
            self._preorder(node.right)


if __name__ == "__main__":
    unittest.main()
