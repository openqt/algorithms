# -*- encoding: utf-8 -*-
'''
Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree2(self, preorder, inorder):
        if len(preorder) == 0: return None

        n = preorder[0]
        node = TreeNode(n)
        pos = inorder.index(n)
        node.left = self.buildTree2(preorder[1:pos+1], inorder[:pos])
        node.right = self.buildTree2(preorder[pos+1:], inorder[pos+1:])
        return node

    def buildTree(self, preorder, inorder):
        return self._build(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def _build(self, preorder, pre_start, pre_stop, inorder, in_start, in_stop):
        if (pre_stop-pre_start) <= 0: return None

        n = preorder[pre_start]
        node = TreeNode(n)
        pos = inorder.index(n, in_start, in_stop)
        l = pos - in_start
        node.left = self._build(preorder, pre_start+1, pre_start+l+1, inorder, in_start, pos)
        node.right = self._build(preorder, pre_start+l+1, pre_stop, inorder, pos+1, in_stop)
        return node


if __name__ == '__main__':
    from TreeNode import *

    s = Solution()
    show(s.buildTree2([1,2,4,5,3], [4,2,5,1,3]))
    print '-' * 30
    show(s.buildTree([1,2,4,5,3], [4,2,5,1,3]))
    print 'PASS'
