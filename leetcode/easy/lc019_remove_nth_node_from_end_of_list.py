'''
Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        pa = pb = head
        for i in range(n):
            pb = pb.next

        if pb is None:
            head = head.next
            return head

        while pb.next is not None:
            pb = pb.next
            pa = pa.next
        pa.next = pa.next.next

        return head


if __name__ == '__main__':
    from utils import ListNode

    s = Solution()
    head = s.removeNthFromEnd(ListNode.toListNode('12345'), 2)
    ListNode.show(head)

    head = s.removeNthFromEnd(ListNode.toListNode('1'), 1)
    ListNode.show(head)

    head = s.removeNthFromEnd(ListNode.toListNode('12'), 2)
    ListNode.show(head)

    print 'PASS'
