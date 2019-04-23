# coding=utf-8
import unittest

"""234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/description/

Given a singly linked list, determine if it is a palindrome.

**Example 1:**

    
    
    **Input:** 1- >2
    **Output:** false

**Example 2:**

    
    
    **Input:** 1- >2->2->1
    **Output:** true

**Follow up:**  
Could you do it in O(n) time and O(1) space?


Similar Questions:
  Palindrome Number (palindrome-number)
  Valid Palindrome (valid-palindrome)
  Reverse Linked List (reverse-linked-list)
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from link import *

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast:  # find the middle point
            fast = fast.next
            if fast and fast.next:
                slow = slow.next
                fast = fast.next
        if not slow: return True
        slow = slow.next  # 下一个节点是后半部分开始

        # reverse 2nd half
        rhead = ListNode(0)
        while slow:
            node = slow.next
            slow.next = rhead.next
            rhead.next = slow
            slow = node

        # compare
        n1, n2 = head, rhead.next
        while n2:
            if n2.val != n1.val: return False
            n1 = n1.next
            n2 = n2.next
        return True


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertFalse(s.isPalindrome(to_node([1,2])))
        self.assertTrue(s.isPalindrome(to_node([0,0])))


if __name__ == "__main__":
    unittest.main()
