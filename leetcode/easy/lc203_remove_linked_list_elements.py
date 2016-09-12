# -*- encoding: utf-8 -*-
'''
Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        p1 = h = ListNode(0)
        p2 = head
        while p2:
            if p2.val != val:
                p1.next = p2
                p1 = p1.next
            p2 = p2.next
        p1.next = None
        return h.next

if __name__ == '__main__':
    from utils.ListNode import *

    s = Solution()
    show(s.removeElements(toListNode('1263456'), '6'))
    show(s.removeElements(toListNode('111'), '1'))
    print 'PASS'
