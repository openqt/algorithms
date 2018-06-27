package main

import "fmt"

/*14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
*/
func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	minlen := len(strs[0])
	for _, s := range strs {
		if len(s) < minlen {
			minlen = len(s)
		}
	}

	for count := 0; count < minlen; count++ {
		c := strs[0][count]
		for _, s := range strs {
			if c != s[count] {
				return s[:count]
			}
		}
	}
	return strs[0][:minlen]
}

func main() {
	fmt.Println()
}
