# coding=utf-8
"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

    For example,

        1
       / \
      2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
from leetcode.utils.funcs import print_result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    @print_result
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.leafs = []
        self.dfs(root, [root.val])
        return sum(self.leafs)

    def dfs(self, node, q):
        if node.left is None and node.right is None:  # leaf
            self.leafs.append(int(''.join(str(i) for i in q)))

        if node.left:
            q.append(node.left.val)
            self.dfs(node.left, q)
            q.pop()

        if node.right:
            q.append(node.right.val)
            self.dfs(node.right, q)
            q.pop()

if __name__ == '__main__':
    from leetcode.utils.binarytree import TreeNode

    s = Solution()
    assert s.sumNumbers(TreeNode.build('123')) == 25
    print 'PASS'
