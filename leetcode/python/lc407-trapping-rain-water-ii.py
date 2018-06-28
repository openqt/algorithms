# coding=utf-8
import unittest

"""407. Trapping Rain Water II
https://leetcode.com/problems/trapping-rain-water-ii/description/

Given an `m x n` matrix of positive integers representing the height of each
unit cell in a 2D elevation map, compute the volume of water it is able to
trap after raining.

**Note:**  
Both _m_ and _n_ are less than 110. The height of each unit cell is greater
than 0 and is less than 20,000.

**Example:**

    
    
    Given the following 3x6 height map:
    [
      [1,4,3,1,3,2],
      [3,2,1,3,2,4],
      [2,3,3,2,3,1]
    ]
    
    Return 4.
    

![](/static/images/problemset/rainwater_empty.png)  
The above image represents the elevation map
`[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]` before the rain.

![](/static/images/problemset/rainwater_fill.png)  
After the rain, water is trapped between the blocks. The total volume of water
trapped is 4.


Similar Questions:
  Trapping Rain Water (trapping-rain-water)
"""


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
