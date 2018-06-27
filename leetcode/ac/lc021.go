package main

/*21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

	Input: 1->2->4, 1->3->4
	Output: 1->1->2->3->4->4

*/
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	h := ListNode{}
	p, p1, p2 := &h, l1, l2
	for ; p1 != nil && p2 != nil; p = p.Next {
		if p1.Val < p2.Val {
			p.Next = p1
			p1 = p1.Next
		} else {
			p.Next = p2
			p2 = p2.Next
		}
	}

	if p2 != nil {
		p1 = p2
	}
	for ; p1 != nil; p1 = p1.Next {
		p.Next = p1
		p = p.Next
	}
	return h.Next
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
}
