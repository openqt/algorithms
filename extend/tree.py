# coding=utf-8
from __future__ import print_function
from collections import deque
import unittest


class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s (%s, %s)' % (repr(self.val),
                                repr(self.left), repr(self.right))


class BinaryTree(object):
    """OJ's Binary Tree Serialization:

    The serialization of a binary tree follows a level order traversal,
    where '#' signifies a path terminator where no node exists below.

    Here's an example:
       1
      / \
     2   3
        /
       4
        \
         5
    The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
    """
    def __init__(self, seq=None):
        self.root = self.set(seq)

    def set(self, seq):
        """从列表形成一个二叉树，此节点作为根节点

        列表构造实际上是一颗满二叉树
        :param seq: binary tree serialization
        :return: tree root node
        """
        if not seq:
            return None
        self.root = TreeNode(seq[0])

        Q = deque([self.root])
        left = True
        for i in seq[1:]:
            if left:
                if not self.stop(i):
                    Q.append(TreeNode(i))
                    Q[0].left = Q[-1]
            else:
                x = Q.popleft()
                if not self.stop(i):
                    Q.append(TreeNode(i))
                    x.right = Q[-1]
            left = not left

        return self.root

    def level_order(self):
        """树结构转为list表示法"""
        seq = []

        Q = deque([self.root])
        while len(Q):
            node = Q.popleft()

            if node:
                seq.append(node.val)
                Q.append(node.left)
                Q.append(node.right)
            else:
                seq.append(self.stop())

        while self.stop(seq[-1]):  # 删除末尾的结束符
            seq.pop()

        return seq

    def stop(self, x=None):
        """get/check stop symbol"""
        if x is None:
            return '#'

        if isinstance(x, TreeNode):
            x = x.val
        return x in ['#']

    def __str__(self):
        """树结构转为字符串表示法"""
        return ','.join(map(str, self.level_order()))

    def pre_order(self):
        seq = []

        def _pre(node):
            if node:
                seq.append(node.val)
                _pre(node.left)
                _pre(node.right)

        _pre(self.root)
        return seq

    def in_order(self):
        seq = []

        def _in(node):
            if node:
                _in(node.left)
                seq.append(node.val)
                _in(node.right)

        _in(self.root)
        return seq

    def post_order(self):
        seq = []

        def _post(node):
            if node:
                _post(node.left)
                _post(node.right)
                seq.append(node.val)

        _post(self.root)
        return seq


class Test(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree('123##4##5')

    def test_level(self):
        self.assertEqual(self.tree.level_order(),
                         ['1', '2', '3', '#', '#', '4', '#', '#', '5'])

    def test_pre(self):
        self.assertEqual(self.tree.pre_order(), ['1', '2', '3', '4', '5'])

    def test_in(self):
        self.assertEqual(self.tree.in_order(), ['2', '1', '4', '5', '3'])

    def test_post(self):
        self.assertEqual(self.tree.post_order(), ['2', '5', '4', '3', '1'])


if __name__ == '__main__':
    unittest.main()
