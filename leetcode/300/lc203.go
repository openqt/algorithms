package main

/*203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/description/

Remove all elements from a linked list of integers that have value val.

Example
	Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
	Return: 1 --> 2 --> 3 --> 4 --> 5
*/
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeElements(head *ListNode, val int) *ListNode {
	h := ListNode{Next: head}
	for p := &h; p.Next != nil; {
		if p.Next.Val == val {
			p.Next = p.Next.Next
		} else {
			p = p.Next
		}
	}
	return h.Next
}

///
type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
}
