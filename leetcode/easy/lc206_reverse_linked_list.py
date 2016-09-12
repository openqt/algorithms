'''
Reverse Linked List

Reverse a singly linked list.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None: return None

        h = p = head
        p = p.next
        h.next = None

        while p:
            t = p.next
            p.next = h

            h = p
            p = t

        return h


if __name__ == '__main__':
    from utils import ListNode

    head = ListNode.toListNode('123456')
    ListNode.show(head)

    s = Solution()
    s.reverseList(ListNode.toListNode(''))

    head = s.reverseList(head)
    ListNode.show(head)

    print 'PASS'
