package main

import (
	"fmt"
)

/*344. Reverse String
https://leetcode.com/problems/reverse-string/description/

Write a function that takes a string as input and returns the string reversed.

Example:
	Given s = "hello", return "olleh".
*/
func reverseString(s string) string {
	n := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		n[i], n[j] = n[j], n[i]
	}
	return string(n)
}

func main() {
	fmt.Println(reverseString("hello") == "olleh")
}
