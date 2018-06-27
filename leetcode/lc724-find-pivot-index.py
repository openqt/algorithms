# coding=utf-8
import unittest

"""Find Pivot Index
https://leetcode.com/problems/find-pivot-index/description/

<p>Given an array of integers <code>nums</code>, write a method that returns the "pivot" index of this array.
</p><p>
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
</p><p>
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
nums = [1, 7, 3, 6, 5, 6]
<b>Output:</b> 3
<b>Explanation:</b> 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
nums = [1, 2, 3]
<b>Output:</b> -1
<b>Explanation:</b> 
There is no index that satisfies the conditions in the problem statement.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>nums</code> will be in the range <code>[0, 10000]</code>.</li>
<li>Each element <code>nums[i]</code> will be an integer in the range <code>[-1000, 1000]</code>.</li>
</p>
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
