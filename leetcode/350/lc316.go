package main

import (
	"fmt"
	"strings"
)

/*316. Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/description/

Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appear once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
	Given "bcabc"
	Return "abc"

	Given "cbacdcbc"
	Return "acdb"
*/
func removeDuplicateLetters(s string) string {
	var book [26]int
	for _, c := range s {
		book[c-'a']++
	}

	key := 0
	for n, c := range s {
		if s[key] > s[n] {
			key = n
		}
		book[c-'a']--
		if book[c-'a'] == 0 {
			ns := strings.Replace(s[key+1:], string(s[key]), "", -1)
			return string(s[key]) + removeDuplicateLetters(ns)
		}
	}
	return ""
}

func main() {
	fmt.Println(removeDuplicateLetters("bcabc") == "abc")
	fmt.Println(removeDuplicateLetters("cbacdcbc") == "acdb")
}
