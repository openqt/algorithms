import unittest
from utils.link import ListNode, to_node


class Solution(unittest.TestCase):
    """2. Add Two Numbers

    You are given two linked lists representing two non-negative numbers. The
    digits are stored in reverse order and each of their nodes contain a single
    digit. Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    """

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def to_int(node):
            val, exp = 0, 1
            while node:
                val += node.val * exp
                exp *= 10
                node = node.next
            return val

        val = to_int(l1) + to_int(l2)

        node = p = ListNode(0)
        if not val:
            return node

        while val:
            p.next = ListNode(val % 10)
            val //= 10
            p = p.next
        return node.next

    def test(self):
        self.assertEqual(self.addTwoNumbers(to_node([0]), to_node([0])),
                         to_node([0]))
        self.assertEqual(
            self.addTwoNumbers(to_node([2, 4, 3]), to_node([5, 6, 4])),
            to_node([7, 0, 8]))


if __name__ == '__main__':
    unittest.main()
