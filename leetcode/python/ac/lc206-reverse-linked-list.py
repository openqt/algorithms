# coding=utf-8
import unittest

"""206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/

Reverse a singly linked list.

**Example:**

    
    
    **Input:** 1- >2->3->4->5->NULL
    **Output:** 5- >4->3->2->1->NULL
    

**Follow up:**

A linked list can be reversed either iteratively or recursively. Could you
implement both?


Similar Questions:
  Reverse Linked List II (reverse-linked-list-ii)
  Binary Tree Upside Down (binary-tree-upside-down)
  Palindrome Linked List (palindrome-linked-list)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from link import *

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        while head:
            n = head.next
            head.next = node.next
            node.next = head
            head = n
        return node.next
        

class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(compare(s.reverseList(to_node("12345")), to_node("54321")))


if __name__ == "__main__":
    unittest.main()
