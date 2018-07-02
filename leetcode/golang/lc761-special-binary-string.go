package main

import (
    "fmt"
)

/*761. Special Binary String
https://leetcode.com/problems/special-binary-string/description/

_Special_ binary strings are binary strings with the following two properties:

* The number of 0's is equal to the number of 1's.
* Every prefix of the binary string has at least as many 1's as 0's.

Given a special string `S`, a _move_ consists of choosing two consecutive,
non-empty, special substrings of `S`, and swapping them. _(Two strings are
consecutive if the last character of the first string is exactly one index
before the first character of the second string.)_

At the end of any number of moves, what is the lexicographically largest
resulting string possible?

**Example 1:**  

    
    
    **Input:** S = "11011000"
    **Output:** "11100100"
    **Explanation:**
    The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
    This is the lexicographically largest string possible after some number of swaps.
    

**Note:**

  1. `S` has length at most `50`.
  2. `S` is guaranteed to be a _special_ binary string as defined above.


Similar Questions:
  Valid Parenthesis String (valid-parenthesis-string)
*/
func makeLargestSpecial(S string) string {
    
}

func main() {
    fmt.Println()
}
