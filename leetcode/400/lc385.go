package main

import (
	"fmt"
)

/*385. Mini Parser
https://leetcode.com/problems/mini-parser/description/

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

	String is non-empty.
	String does not contain white spaces.
	String contains only digits 0-9, [, - ,, ].

Example 1:

	Given s = "324",
	You should return a NestedInteger object which contains a single integer 324.

Example 2:

	Given s = "[123,[456,[789]]]",
	Return a NestedInteger object containing a nested list with 2 elements:
	1. An integer containing value 123.
	2. A nested list containing two elements:
		i.  An integer containing value 456.
		ii. A nested list with one element:
			 a. An integer containing value 789.
*/
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (n NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (n NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (n *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (n NestedInteger) GetList() []*NestedInteger {}
 */
func deserialize(s string) *NestedInteger {
	ni, _ := atoNI(s)
	return &ni
}

func atoi(s string) (n, i int) {
	neg := false
	if s[i] == '-' {
		neg = true
		i++
	}
	for ; i < len(s) && ('0' <= s[i] && s[i] <= '9'); i++ {
		n = n*10 + int(s[i]-'0')
	}
	if neg {
		return -n, i
	}
	return n, i
}

func atoNI(s string) (NestedInteger, int) {
	ni, pos := NestedInteger{}, 0
	state := '-'
	for pos < len(s) {
		switch s[pos] {
		case '[':
			if state == '[' {
				val, i := atoNI(s[pos:])
				ni.Add(val)
				pos += i
			} else {
				state = '['
				pos++
			}
		case ']':
			return ni, pos + 1
		case ',', ' ':
			pos++
		default:
			val, i := atoi(s[pos:])
			pos += i
			if state == '[' {
				nv := NestedInteger{}
				nv.SetInteger(val)
				ni.Add(nv)
			} else {
				ni.SetInteger(val)
			}
		}
	}
	return ni, pos
}

/////
// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
type NestedInteger struct {
	Value int
	List  []*NestedInteger
	isInt bool
}

// Return true if this NestedInteger holds a single integer, rather than a nested list.
func (n NestedInteger) IsInteger() bool {
	return n.isInt
}

// Return the single integer that this NestedInteger holds, if it holds a single integer
// The result is undefined if this NestedInteger holds a nested list
// So before calling this method, you should have a check
func (n NestedInteger) GetInteger() int {
	return n.Value
}

// Set this NestedInteger to hold a single integer.
func (n *NestedInteger) SetInteger(value int) {
	n.Value = value
	n.isInt = true
}

// Set this NestedInteger to hold a nested list and adds a nested integer to it.
func (n *NestedInteger) Add(elem NestedInteger) {
	n.List = append(n.List, &elem)
	n.isInt = false
}

// Return the nested list that this NestedInteger holds, if it holds a nested list
// The list length is zero if this NestedInteger holds a single integer
// You can access NestedInteger's List element directly if you want to modify it
func (n NestedInteger) GetList() []*NestedInteger {
	return n.List
}

func NItoa(ni *NestedInteger) string {
	s := ""
	if ni != nil {
		if ni.IsInteger() {
			s += fmt.Sprintf("%d", ni.Value)
		} else {
			s += "["
			for n, i := range ni.GetList() {
				s += NItoa(i)
				if n < len(ni.GetList())-1 {
					s += ","
				}
			}
			s += "]"
		}
	}
	return s
}

func main() {
	fmt.Println(NItoa(deserialize("[]")) == "[]")
	fmt.Println(NItoa(deserialize("[[]]")) == "[[]]")
	fmt.Println(NItoa(deserialize("324")) == "324")
	fmt.Println(NItoa(deserialize("[123,[456,[789]]]")) == "[123,[456,[789]]]")
	fmt.Println(NItoa(deserialize("[123,456]")) == "[123,456]")
	fmt.Println(NItoa(deserialize("[123,456,[788,799,833],[[]],10,[]]")) == "[123,456,[788,799,833],[[]],10,[]]")
}
