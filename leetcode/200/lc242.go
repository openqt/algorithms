package main

import (
	"fmt"
)

/*242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
	s = "anagram", t = "nagaram", return true.
	s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
*/
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	var sa, ta [26]int
	for i := 0; i < len(s); i++ {
		sa[s[i]-'a']++
		ta[t[i]-'a']++
	}
	return sa == ta
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
	fmt.Println(!isAnagram("rat", "car"))
}
