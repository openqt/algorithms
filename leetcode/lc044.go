package main

import (
	"fmt"
)

/*
Implement wildcard pattern matching with support for '?' and '*'.

	'?' Matches any single character.
	'*' Matches any sequence of characters (including the empty sequence).

	The matching should cover the entire input string (not partial).

	The function prototype should be:
	bool isMatch(const char *s, const char *p)

	Some examples:
	isMatch("aa","a") → false
	isMatch("aa","aa") → true
	isMatch("aaa","aa") → false
	isMatch("aa", "*") → true
	isMatch("aa", "a*") → true
	isMatch("ab", "?*") → true
	isMatch("aab", "c*a*b") → false
*/
func isMatch(s, p string) bool {
	var si, pi int
	flag := false
	si2, pi2 := len(s), len(p)
	for si < len(s) {
		if pi < len(p) && p[pi] == '*' {
			flag = true
			pi += 1
			si2 = si
			pi2 = pi
		} else if pi < len(p) && (p[pi] == '?' || p[pi] == s[si]) {
			si++
			pi++
		} else if flag {
			si2 += 1
			si = si2

			pi = pi2
		} else {
			return false
		}
	}
	for ; pi < len(p) && p[pi] == '*'; pi++ {
	}
	return pi == len(p)
}

// 参考：http://blog.csdn.net/makuiyu/article/details/43698963
func main() {
	fmt.Println(isMatch("", "") == true)
	fmt.Println(isMatch("", "*") == true)
	fmt.Println(isMatch("aa", "a") == false)
	fmt.Println(isMatch("aa", "aa") == true)
	fmt.Println(isMatch("aaa", "aa") == false)
	fmt.Println(isMatch("aa", "*") == true)
	fmt.Println(isMatch("ab", "?*") == true)
	fmt.Println(isMatch("aab", "c*a*b") == false)

	fmt.Println(isMatch("a1a2a3a4a5b1", "a6*b2") == false)
	fmt.Println(isMatch("aaaaab", "a*ab") == true)
	fmt.Println(isMatch("a", "a*a") == false)
	fmt.Println(isMatch("a", "ab*") == false)
	fmt.Println(isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b") == false)
	fmt.Println(isMatch("zacabz", "*a?b*") == false)
	fmt.Println(isMatch("aaaa", "***a") == true)
}
