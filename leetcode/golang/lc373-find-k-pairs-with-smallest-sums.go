package main

import (
    "fmt"
)

/*373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

You are given two integer arrays **nums1** and **nums2** sorted in ascending
order and an integer **k**.

Define a pair **(u,v)** which consists of one element from the first array and
one element from the second array.

Find the k pairs **(u 1,v1),(u2,v2) ...(uk,vk)** with the smallest sums.

**Example 1:**  

    
    
    Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
    
    Return: [1,2],[1,4],[1,6]
    
    The first 3 pairs are returned from the sequence:
    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
    

**Example 2:**  

    
    
    Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2
    
    Return: [1,1],[1,1]
    
    The first 2 pairs are returned from the sequence:
    [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
    

**Example 3:**  

    
    
    Given nums1 = [1,2], nums2 = [3],  k = 3 
    
    Return: [1,3],[2,3]
    
    All possible pairs are returned from the sequence:
    [1,3],[2,3]
    

**Credits:**  
Special thanks to [@elmirap](https://leetcode.com/elmirap/) and
[@StefanPochmann](https://leetcode.com/stefanpochmann/) for adding this
problem and creating all test cases.


Similar Questions:
  Kth Smallest Element in a Sorted Matrix (kth-smallest-element-in-a-sorted-matrix)
  Find K-th Smallest Pair Distance (find-k-th-smallest-pair-distance)
*/
func kSmallestPairs(nums1 []int, nums2 []int, k int) [][]int {
    
}

func main() {
    fmt.Println()
}
