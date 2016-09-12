'''
Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

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
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree2(self, inorder, postorder):
        if len(postorder) == 0: return None

        n = postorder[-1]
        node = TreeNode(n)
        pos = inorder.index(n)
        node.left = self.buildTree2(inorder[:pos], postorder[:pos])
        node.right = self.buildTree2(inorder[pos+1:], postorder[pos:-1])
        return node

    def buildTree(self, inorder, postorder):
        return self._build(inorder, 0, len(inorder), postorder, 0, len(postorder))

    def _build(self, inorder, in_start, in_stop, postorder, post_start, post_stop):
        if (in_stop-in_start) <= 0: return None

        n = postorder[post_stop-1]
        node = TreeNode(n)
        pos = inorder.index(n, in_start, in_stop)
        l = pos - in_start
        node.left = self._build(inorder, in_start, pos, postorder, post_start, post_start+l)
        node.right = self._build(inorder, pos+1, in_stop, postorder, post_start+l, post_stop-1)
        return node


if __name__ == '__main__':
    from TreeNode import *

    s = Solution()
    show(s.buildTree2([4,2,5,1,3], [4,5,2,3,1]))
    print '-' * 30
    show(s.buildTree([4,2,5,1,3], [4,5,2,3,1]))
    print 'PASS'
