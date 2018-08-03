package main

import "fmt"

/*3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string, find the length of the **longest substring** without repeating
characters.

**Examples:**

Given `"abcabcbb"`, the answer is `"abc"`, which the length is 3.

Given `"bbbbb"`, the answer is `"b"`, with the length of 1.

Given `"pwwkew"`, the answer is `"wke"`, with the length of 3. Note that the
answer must be a **substring** , `"pwke"` is a _subsequence_ and not a
substring.


Similar Questions:
  Longest Substring with At Most Two Distinct Characters (longest-substring-with-at-most-two-distinct-characters)
*/

/* https://leetcode.com/articles/longest-substring-without-repeating-characters/

Approach 2: Sliding Window

A sliding window is an abstract concept commonly used in array/string problems.
A window is a range of elements in the array/string which usually defined by the start and end indices,
i.e. [i, j)[i,j) (left-closed, right-open).
A sliding window is a window "slides" its two boundaries to the certain direction. For example,
if we slide [i, j)[i,j) to the right by 11 element, then it becomes [i+1, j+1)[i+1,j+1) (left-closed, right-open).
 */
func lengthOfLongestSubstring(s string) int {
    cache := make(map[byte]int)
    val, i := 0, 0
    for j := 0; j < len(s); {
        c := s[j]
        if _, ok := cache[c]; !ok {
            cache[c] = j
            j += 1

            if j-i > val {
                val = j - i
            }
        } else {
            delete(cache, s[i])
            i += 1

        }
    }
    return val
}

func main() {
    fmt.Println(lengthOfLongestSubstring("abcabcbb") == 3)
    fmt.Println(lengthOfLongestSubstring("pwwkew") == 3)
    fmt.Println(lengthOfLongestSubstring("c") == 1)
}
