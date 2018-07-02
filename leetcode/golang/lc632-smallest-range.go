package main

import (
    "fmt"
)

/*632. Smallest Range
https://leetcode.com/problems/smallest-range/description/

You have `k` lists of sorted integers in ascending order. Find the
**smallest** range that includes at least one number from each of the `k`
lists.

We define the range [a,b] is smaller than range [c,d] if `b-a < d-c` or `a <
c` if `b-a == d-c`.

**Example 1:**  

    
    
    **Input:** [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    **Output:** [20,24]
    **Explanation:** 
    List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
    List 2: [0, 9, 12, 20], 20 is in range [20,24].
    List 3: [5, 18, 22, 30], 22 is in range [20,24].
    

**Note:**  

  1. The given list may contain duplicates, so ascending order means >= here.
  2. 1 <= `k` <= 3500
  3. -105 <= `value of elements` <= 105.
  4. **For Java users, please note that the input type has been changed to List <List<Integer>>. And after you reset the code template, you'll see this point.**


Similar Questions:
  Minimum Window Substring (minimum-window-substring)
*/
func smallestRange(nums [][]int) []int {
    
}

func main() {
    fmt.Println()
}
