package main

import (
	"fmt"
)

/*567. Permutation in String
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
	Input:s1 = "ab" s2 = "eidbaooo"
	Output:True
	Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
	Input:s1= "ab" s2 = "eidboaoo"
	Output: False

Note:
	The input strings only contain lower case letters.
	The length of both given strings is in range [1, 10,000].
*/
func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	base, window := [26]int{}, [26]int{}
	size := len(s1)
	for i := 0; i < size; i++ {
		base[s1[i]-'a']++
		window[s2[i]-'a']++
	}
	if window == base {
		return true
	}

	for i := size; i < len(s2); i++ {
		window[s2[i-size]-'a']--
		window[s2[i]-'a']++
		if window == base {
			return true
		}
	}

	return false
}

func main() {
	fmt.Println(checkInclusion("ab", "ab") == true)
	fmt.Println(checkInclusion("ab", "a") == false)
	fmt.Println(checkInclusion("ab", "eidbaooo") == true)
	fmt.Println(checkInclusion("ab", "eidboaoo") == false)
}
