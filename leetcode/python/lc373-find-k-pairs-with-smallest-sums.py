# coding=utf-8
import unittest

"""373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

<p>
You are given two integer arrays <b>nums1</b> and <b>nums2</b> sorted in ascending order and an integer <b>k</b>. 
</p>

<p>Define a pair <b>(u,v)</b> which consists of one element from the first array and one element from the second array.</p>

<p>Find the k pairs <b>(u<sub>1</sub>,v<sub>1</sub>),(u<sub>2</sub>,v<sub>2</sub>) ...(u<sub>k</sub>,v<sub>k</sub>)</b> with the smallest sums.
</p>

<p><b>Example 1:</b><br />
<pre>
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
</pre>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/elmirap/">@elmirap</a> and <a href="https://leetcode.com/stefanpochmann/">@StefanPochmann</a> for adding this problem and creating all test cases.</p>
Similar Questions:
  Kth Smallest Element in a Sorted Matrix (kth-smallest-element-in-a-sorted-matrix)
  Find K-th Smallest Pair Distance (find-k-th-smallest-pair-distance)
"""


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
