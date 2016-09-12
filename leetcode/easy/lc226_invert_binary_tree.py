# -*- encoding: utf-8 -*-
'''
Invert Binary Tree

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None: return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    from utils import TreeNode
    node = TreeNode.toTreeNode('1234567')
    TreeNode.show(node)

    s = Solution()
    TreeNode.show(s.invertTree(node))

    TreeNode.show(s.invertTree(TreeNode.toTreeNode('1')))

    node = TreeNode.toTreeNode('4271369')
    TreeNode.show(node)
    TreeNode.show(s.invertTree(node))
    print 'PASS'
