package main

import "fmt"

/*20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
	Input: "()"
	Output: true

Example 2:
	Input: "()[]{}"
	Output: true

Example 3:
	Input: "(]"
	Output: false

Example 4:
	Input: "([)]"
	Output: false

Example 5:
	Input: "{[]}"
	Output: true
*/
func isValid(s string) bool {
	stack, p := make([]rune, len(s)), 0
	table := map[rune]rune{')': '(', ']': '[', '}': '{'}
	for _, c := range s {
		switch c {
		case '(', '[', '{':
			stack[p] = c
			p++
		default:
			if p > 0 && table[c] == stack[p-1] {
				p--
			} else {
				return false
			}
		}
	}
	return p == 0
}

func main() {
	fmt.Println(!isValid("["))
	fmt.Println(isValid("()"))
	fmt.Println(isValid("()[]{}"))
	fmt.Println(!isValid("(]"))
	fmt.Println(!isValid("([)]"))
	fmt.Println(isValid("{[]}"))
}
