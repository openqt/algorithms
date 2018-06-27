# coding=utf-8
import unittest

"""382. Linked List Random Node
https://leetcode.com/problems/linked-list-random-node/description/

<p>Given a singly linked list, return a random node's value from the linked list. Each node must have the <b>same probability</b> of being chosen.</p>

<p><b>Follow up:</b><br />
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
</p>

<p><b>Example:</b>
<pre>
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
</pre>
</p>
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
