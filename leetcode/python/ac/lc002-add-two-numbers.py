# coding=utf-8
import unittest

"""2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/

You are given two **non-empty** linked lists representing two non-negative
integers. The digits are stored in **reverse order** and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

**Example**

    
    
    **Input:** (2 -> 4 -> 3) + (5 -> 6 -> 4)
    **Output:** 7 -> 0 -> 8
    **Explanation:** 342 + 465 = 807.


Similar Questions:
  Multiply Strings (multiply-strings)
  Add Binary (add-binary)
  Sum of Two Integers (sum-of-two-integers)
  Add Strings (add-strings)
  Add Two Numbers II (add-two-numbers-ii)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from link import ListNode, to_node, compare


class Solution(unittest.TestCase):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def toint(node):
            val, p, level = 0, node, 1
            while p:
                val += p.val * level
                level *= 10
                p = p.next
            return val

        def tolist(n):
            head = ListNode(0)
            p = head
            while n > 0:
                p.next = ListNode(n % 10)
                p = p.next
                n /= 10
            return head.next or head

        return tolist(toint(l1) + toint(l2))

    def test(self):
        self.assertTrue(compare(
            self.addTwoNumbers(to_node([0]), to_node([0])), to_node([0])))
        self.assertTrue(compare(
            self.addTwoNumbers(to_node([2, 4, 3]), to_node([5, 6, 4])),
            to_node([7, 0, 8])))


if __name__ == "__main__":
    unittest.main()
