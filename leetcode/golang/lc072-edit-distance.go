package main

import (
    "fmt"
)

/*72. Edit Distance
https://leetcode.com/problems/edit-distance/description/

Given two words _word1_ and _word2_ , find the minimum number of operations
required to convert _word1_ to _word2_.

You have the following 3 operations permitted on a word:

  1. Insert a character
  2. Delete a character
  3. Replace a character

**Example 1:**

    
    
    **Input:** word1 =  "horse", word2 = "ros"
    **Output:** 3
    **Explanation:** 
    horse - > rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')
    

**Example 2:**

    
    
    **Input:** word1 =  "intention", word2 = "execution"
    **Output:** 5
    **Explanation:** 
    intention - > inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')


Similar Questions:
  One Edit Distance (one-edit-distance)
  Delete Operation for Two Strings (delete-operation-for-two-strings)
  Minimum ASCII Delete Sum for Two Strings (minimum-ascii-delete-sum-for-two-strings)
*/
func minDistance(word1 string, word2 string) int {
    
}

func main() {
    fmt.Println()
}
