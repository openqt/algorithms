package main

import (
	"fmt"
)

/*80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

Given a sorted array _nums_ , remove the duplicates [**in-
place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that
duplicates appeared at most  _twice_ and return the new length.

Do not allocate extra space for another array, you must do this by **modifying
the input array[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**
with O(1) extra memory.

**Example 1:**

    
    
    Given _nums_ = **[1,1,1,2,2,3]** ,
    
    Your function should return length = **5** , with the first five elements of _nums_ being **1, 1, 2, 2** and **3** respectively.
    
    It doesn 't matter what you leave beyond the returned length.

**Example 2:**

    
    
    Given _nums_ = **[0,0,1,1,1,1,2,3,3]** ,
    
    Your function should return length = **7** , with the first seven elements of _nums_ being modified to   **0** , **0** , **1** , **1** , **2** , **3** and   **3** respectively.
    
    It doesn 't matter what values are set beyond the returned length.
    

**Clarification:**

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by **reference** , which means
modification to the input array will be known to the caller as well.

Internally you can think of this:

    
    
    // **nums** is passed in by reference. (i.e., without making a copy)
    int len = removeDuplicates(nums);
    
    // any modification to **nums** in your function would be known by the caller.
    // using the length returned by your function, it prints the first **len** elements.
    for (int i = 0; i  < len; i++) {
        print(nums[i]);
    }


Similar Questions:
  Remove Duplicates from Sorted Array (remove-duplicates-from-sorted-array)
*/
func removeDuplicates(nums []int) int {
    
}

func main() {
	fmt.Println()
}
