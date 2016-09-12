'''
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root: return True
        if abs(self._depth(root.left) - self._depth(root.right)) > 1: return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        # return self._differ(root) != -1

    def _depth(self, root):
        if not root: return 0
        return max(self._depth(root.left), self._depth(root.right)) + 1

    # def _differ(self, root):
    #     if not root: return 0
    #     l = self._differ(root.left)
    #     if l < 0: return -1
    #     r = self._differ(root.right)
    #     if r < 0: return -1
    #     if abs(l - r) > 1: return -1
    #     return max(l, r) + 1


if __name__ == '__main__':
    from TreeNode import *
    s = Solution()
    node = toTreeNode('12')
    print s.isBalanced(node)

    node = toTreeNode('1#2#3')
    print not s.isBalanced(node)

    node = toTreeNode('1223##34##4')
    print not s.isBalanced(node)

    node = toTreeNode('12233##44')
    print not s.isBalanced(node)

    node = toTreeNode('1223333444444##55')
    print s.isBalanced(node)

    print 'PASS'
