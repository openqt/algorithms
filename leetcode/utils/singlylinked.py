# coding=utf-8
# Definition for singly-linked node


class ListNode:
    """
    OJ singly-linked list
    默认头节点即第一个元素节点
    """

    def __init__(self, x):
        if isinstance(x, ListNode):
            self.val, self.next = x.val, x.next
        else:
            self.val, self.next = x, None

    @staticmethod
    def build(seq):
        """
        从可遍历对象构造单链表结构
        :param seq: 壳遍历对象
        :return: 单链表头节点
        """
        p = head = ListNode(None)
        for i in seq:
            p.next = ListNode(i)
            p = p.next
        return head.next

    def __str__(self):
        """
        当前链表转为字符串表示：
            a > b > c > d > e > f > g > END
        :return:
        """
        p = self
        s = '{}: '.format(id(self))
        while p:
            s += '{} > '.format(p.val)
            p = p.next
        s += 'END[{0:X}]'.format(id(self))
        return s

    def copy(self):
        """
        复制链表，从当前节点开始复制
        :return: 新链表的头节点
        """
        node1 = self
        head = node2 = ListNode(0)
        while node1:
            node2.next = ListNode(node1)
            node1 = node1.next
            node2 = node2.next
        return head.next

    def __reversed__(self):
        """
        逆序链表，返回新的头节点，之前链表会被破坏
        :return: 新的逆序后的头节点
        """
        head = ListNode(0)
        node = self
        while node:
            t = node.next
            node.next = head.next
            head.next = node
            node = t
        return head.next


if __name__ == '__main__':
    node = ListNode.build('abcdefg')
    print node
    print reversed(node.copy())
    print node

