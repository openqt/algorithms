# coding=utf-8
from __future__ import print_function
import unittest


class ListNode(object):
    """Definition for singly-linked list."""

    def __init__(self, x):
        if isinstance(x, ListNode):
            self.val, self.next = x.val, x.next
        else:
            self.val, self.next = x, None

    def __eq__(self, other):
        """=="""
        p = self
        while p and other:
            if p.val != other.val:
                return False
            p = p.next
            other = other.next
        return not (p or other)


class LinkedList(object):
    """OJ singly-linked list

    默认头节点即第一个元素节点
    """

    def __init__(self, seq=None):
        self.head = None
        self.set(seq)

    def set(self, seq):
        """从可遍历对象构造单链表结构

        :param seq: 壳遍历对象
        :return: 单链表头节点
        """
        head = p = ListNode(None)
        for i in seq:
            p.next = ListNode(i)
            p = p.next
        self.head = head.next

        return self

    def __str__(self):
        """当前链表转为字符串表示

        :return: a > b > c > d > e > f > g > END
        """
        return str(self.to_list())

    def to_list(self):
        seq = []
        p = self.head
        while p:
            seq.append(p.val)
            p = p.next
        return seq

    def copy(self):
        """复制链表，从当前节点开始复制

        :return: 新链表的头节点
        """
        return LinkedList(self.to_list())

    def __reversed__(self):
        """逆序链表，返回新的头节点，之前链表会被破坏

        :return: 新的逆序后的头节点
        """
        head = ListNode(0)
        node = self.head
        while node:
            t = node.next
            node.next = head.next
            head.next = node
            node = t
        self.head = head.next

        return self

    def __eq__(self, other):
        """=="""
        return self.head == other.head


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_str(self):
        link = LinkedList('abcdef')
        self.assertEqual(str(link), "['a', 'b', 'c', 'd', 'e', 'f']")

    def test_copy(self):
        link = LinkedList('abcdef')
        copy = link.copy()
        self.assertNotEqual(id(link), id(copy))
        self.assertEqual(str(copy), "['a', 'b', 'c', 'd', 'e', 'f']")

    def test_reverse(self):
        link = LinkedList('abcdef')
        self.assertEqual(str(reversed(link)),
                         "['f', 'e', 'd', 'c', 'b', 'a']")

    def test_eq(self):
        self.assertEqual(LinkedList('abc'), LinkedList('abc'))
        self.assertNotEqual(LinkedList('ab'), LinkedList('abc'))


def to_node(seq):
    return LinkedList(seq).head


def compare(l1, l2):
    p1, p2 = l1, l2
    while p1 and p2 and p1.val == p2.val:
        p1 = p1.next
        p2 = p2.next

    return not p1 and not p2


if __name__ == '__main__':
    unittest.main()
