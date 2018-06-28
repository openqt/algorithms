# coding=utf-8
import unittest

"""26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given a sorted array _nums_ , remove the duplicates [**in-
place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each
element appear only _once_ and return the new length.

Do not allocate extra space for another array, you must do this by **modifying
the input array[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**
with O(1) extra memory.

**Example 1:**

    
    
    Given _nums_ = **[1,1,2]** ,
    
    Your function should return length = **2** , with the first two elements of _nums_ being **1** and **2** respectively.
    
    It doesn 't matter what you leave beyond the returned length.

**Example 2:**

    
    
    Given _nums_ = **[0,0,1,1,1,2,2,3,3,4]** ,
    
    Your function should return length = **5** , with the first five elements of _nums_ being modified to   **0** , **1** , **2** , **3** , and  **4** respectively.
    
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
  Remove Element (remove-element)
  Remove Duplicates from Sorted Array II (remove-duplicates-from-sorted-array-ii)
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()