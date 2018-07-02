package main

import (
    "fmt"
)

/*239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/description/

Given an array _nums_ , there is a sliding window of size _k_ which is moving
from the very left of the array to the very right. You can only see the _k_
numbers in the window. Each time the sliding window moves right by one
position. Return the max sliding window.

**Example:**

    
    
    **Input:** _nums_ = [1,3,-1,-3,5,3,6,7], and _k_ = 3
    **Output:**[3,3,5,5,6,7] 
    **Explanation:**
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       **3**
     1 [3  -1  -3] 5  3  6  7       **3**
     1  3 [-1  -3  5] 3  6  7      **5**
     1  3  -1 [-3  5  3] 6  7       **5**
     1  3  -1  -3 [5  3  6] 7       **6**
     1  3  -1  -3  5 [3  6  7]      **7**
    

**Note:**  
You may assume _k_ is always valid, 1  ≤ k ≤ input array's size for non-empty
array.

**Follow up:**  
Could you solve it in linear time?


Similar Questions:
  Minimum Window Substring (minimum-window-substring)
  Min Stack (min-stack)
  Longest Substring with At Most Two Distinct Characters (longest-substring-with-at-most-two-distinct-characters)
  Paint House II (paint-house-ii)
*/
func maxSlidingWindow(nums []int, k int) []int {
    
}

func main() {
    fmt.Println()
}
