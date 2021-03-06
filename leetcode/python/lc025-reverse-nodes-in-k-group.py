# coding=utf-8
import unittest

"""25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Given a linked list, reverse the nodes of a linked list _k_ at a time and
return its modified list.

_k_ is a positive integer and is less than or equal to the length of the
linked list. If the number of nodes is not a multiple of _k_ then left-out
nodes in the end should remain as it is.

**Example:**

Given this linked list: `1->2->3->4->5`

For _k_ = 2, you should return: `2->1->4->3->5`

For _k_ = 3, you should return: `3->2->1->4->5`

**Note:**

  * Only constant extra memory is allowed.
  * You may not alter the values in the list's nodes, only nodes itself may be changed.


Similar Questions:
  Swap Nodes in Pairs (swap-nodes-in-pairs)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
