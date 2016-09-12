'''
Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        p = h = ListNode(None)
        while head:
            if head.val != p.val:
                p.next = head
                p = p.next
            head = head.next
        p.next = None

        return h.next


if __name__ == '__main__':
    s = Solution()
    print 'PASS'
