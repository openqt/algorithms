package main

import (
    "fmt"
)

/*2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/

You are given two **non-empty** linked lists representing two non-negative
integers. The digits are stored in **reverse order** and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

**Example**

    
    
    **Input:** (2 -> 4 -> 3) + (5 -> 6 -> 4)
    **Output:** 7 -> 0 -> 8
    **Explanation:** 342 + 465 = 807.


Similar Questions:
  Multiply Strings (multiply-strings)
  Add Binary (add-binary)
  Sum of Two Integers (sum-of-two-integers)
  Add Strings (add-strings)
  Add Two Numbers II (add-two-numbers-ii)
*/

// Definition for singly-linked list.
type ListNode struct {
    Val  int
    Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    head := ListNode{}
    p, carry := &head, 0
    for p1, p2 := l1, l2; p1 != nil || p2 != nil; {
        v1 := 0
        if p1 != nil {
            v1 = p1.Val
            p1 = p1.Next
        }
        v2 := 0
        if p2 != nil {
            v2 = p2.Val
            p2 = p2.Next
        }
        sum := v1 + v2 + carry
        carry = sum / 10
        node := new(ListNode)
        node.Val = sum % 10
        p.Next = node
        p = p.Next
    }
    if carry > 0 {
        p.Next = new(ListNode)
        p.Next.Val = carry
    }
    return head.Next
}

func main() {
    fmt.Println()
}
