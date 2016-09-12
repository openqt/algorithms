'''
Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
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
    # def isValidBST(self, root):
    #     if root is None: return True
    #     if self._less(root.left, root) and self._great(root.right, root):
    #         return self.isValidBST(root.left) and self.isValidBST(root.right)
    #     print root, root.left, root.right
    #     return False
    #
    # def _less(self, root, node):
    #     if root is None: return True
    #     if not (root.val < node.val): return False
    #     return self._less(root.left, node) and self._less(root.right, node)
    #
    # def _great(self, root, node):
    #     if root is None: return True
    #     if not (root.val > node.val): return False
    #     return self._great(root.left, node) and self._great(root.right, node)

    def isValidBST(self, root):
        return self._dfs(root, -2147483648-1, 2147483647+1)

    def _dfs(self, root, _min, _max):
        if root is None: return True
        if _min < root.val < _max:
            return self._dfs(root.left, _min, root.val) and self._dfs(root.right, root.val, _max)
        return False


if __name__ == '__main__':
    from TreeNode import *

    s = Solution()
    print not s.isValidBST(toTreeNode([1,'#',2,3]))
    print not s.isValidBST(toTreeNode([10,5,15,'#','#',6,20]))
    print s.isValidBST(toTreeNode([int(i) for i in '3150246']))
    print 'PASS'
