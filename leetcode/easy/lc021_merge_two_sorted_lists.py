'''
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1: node.next = l1
        if l2: node.next = l2
        return head.next


if __name__ == '__main__':
    from utils.ListNode import *
    s = Solution()
    show(s.mergeTwoLists(toListNode('1357'), toListNode('2468')))
    print 'PASS'
