# coding=utf-8
import unittest

"""430. Flatten a Multilevel Doubly Linked List
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/

You are given a doubly linked list which in addition to the next and previous
pointers, it could have a child pointer, which may or may not point to a
separate doubly linked list. These child lists may have one or more children
of their own, and so on, to produce a multilevel data structure, as shown in
the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked
list. You are given the head of the first level of the list.

**Example:**

    
    
    **Input:**
     1---2---3---4---5---6--NULL
             |
             7---8---9---10--NULL
                 |
                 11--12--NULL
    
    **Output:**
    1-2-3-7-8-11-12-9-10-4-5-6-NULL
    

**Explanation for the above example:**

Given the following multilevel doubly linked list:

![](/static/images/problemset/MultilevelLinkedList.png)

We should return the following flattened doubly linked list:

![](/static/images/problemset/MultilevelLinkedListFlattened.png)


Similar Questions:
  Flatten Binary Tree to Linked List (flatten-binary-tree-to-linked-list)
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
