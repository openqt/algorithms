# -*- encoding: utf-8 -*-
'''
Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the
lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        la = self._pre(root, p)
        lb = self._pre(root, q)
        node = None
        for a, b in zip(la, lb):
            if a != b:
                break
            node = a
        return node

    def _pre(self, root, node, l=None):
        if root is None: return None
        if l is None: l = []
        l.append(root)
        if l[-1] != node:
            if not self._pre(root.left, node, l) and not self._pre(root.right, node, l):
                l.pop()
                return None
        return l


    # def lowestCommonAncestor(self, root, p, q):
    #     if root is None or root == p or root == q:
    #         return root
    #     ln = self.lowestCommonAncestor(root.left, p, q)
    #     rn = self.lowestCommonAncestor(root.right, p, q)
    #     if ln and rn:
    #         return root
    #     return ln if ln is not None else rn

if __name__ == '__main__':
    from TreeNode import *

    s = Solution()
    # print s.lowestCommonAncestor(toTreeNode('3516208##74'), TreeNode('5'), TreeNode('4')).val == '5'
    # print s.lowestCommonAncestor(toTreeNode([37,-34,-48,'#',-100,-100,48,'#','#','#','#',-54,'#',-71,-22,'#','#','#',8]),
    #                              TreeNode(-100), TreeNode(-71)).val# == -48
    # print s.lowestCommonAncestor(toTreeNode([37,-34,-48,'#',-100,-100,48,'#','#','#','#',-54,'#',-71,-22,'#','#','#',8]),
    #                                         TreeNode(-100), TreeNode(-100)).val == 37
    print 'PASS'
