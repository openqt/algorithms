# coding=utf-8
"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
    Could you do it in O(n) time and O(1) space?
"""
from leetcode.utils.funcs import print_result
from leetcode.utils.singlylinked import ListNode


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    @print_result
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        slow = fast = head
        # 快慢指针找到链表中点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 逆序后半部分
        node = slow.next
        slow.next = None  # 设置终止点
        while node:  # 有下一个节点
            fast = node.next
            node.next = slow.next
            slow.next = node
            node = fast

        slow, fast = head, slow.next  # 重设快慢指针到开始位置
        while slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(ListNode.build('12321'))
    assert s.isPalindrome(ListNode.build('123321'))
    assert not s.isPalindrome(ListNode.build('12322'))
    print 'PASS'
