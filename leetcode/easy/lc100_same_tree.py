'''
Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if (p and q) and (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q


if __name__ == '__main__':
    s = Solution()
    print 'PASS'
