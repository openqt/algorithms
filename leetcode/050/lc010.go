package main

import (
	"fmt"
)

/* 10. Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.

	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.

	The matching should cover the entire input string (not partial).

	The function prototype should be:
	bool isMatch(const char *s, const char *p)

	Some examples:
	isMatch("aa","a") → false
	isMatch("aa","aa") → true
	isMatch("aaa","aa") → false
	isMatch("aa", "a*") → true
	isMatch("aa", ".*") → true
	isMatch("ab", ".*") → true
	isMatch("aab", "c*a*b") → true
*/
func isMatch(s, p string) bool {
	var si, pi int
	for pi < len(p) {
		if pi+1 < len(p) && p[pi+1] == '*' {
			for ; si < len(s) && (p[pi] == '.' || p[pi] == s[si]); si++ {
				if isMatch(s[si:], p[pi+2:]) { // * match 0+
					return true
				}
			}
			pi += 2
		} else if si < len(s) && (p[pi] == '.' || p[pi] == s[si]) {
			si++
			pi++
		} else {
			return false
		}
	}
	return si == len(s) && pi == len(p)
}

// http://www.bubuko.com/infodetail-604758.html
func main() {
	fmt.Println(isMatch("", "") == true)
	fmt.Println(isMatch("aa", "a") == false)
	fmt.Println(isMatch("aa", "aa") == true)
	fmt.Println(isMatch("aaa", "aa") == false)
	fmt.Println(isMatch("aa", "a*") == true)
	fmt.Println(isMatch("aa", ".*") == true)
	fmt.Println(isMatch("ab", ".*") == true)
	fmt.Println(isMatch("aab", "c*a*b") == true)

	fmt.Println(isMatch("a1a2a3a4a5b1", "a6*b2") == false)
	fmt.Println(isMatch("aaaaab", "a*ab") == true)
	fmt.Println(isMatch("a", "a*a") == true)
	fmt.Println(isMatch("a", "ab*") == true)
}
