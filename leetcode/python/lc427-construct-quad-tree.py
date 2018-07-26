# coding=utf-8
import unittest

"""427. Construct Quad Tree
https://leetcode.com/problems/construct-quad-tree/description/

We want to use quad trees to store an `N x N` boolean grid. Each cell in the
grid can only be true or false. The root node represents the whole grid. For
each node, it will be subdivided into four children nodes **until the values
in the region it represents are all the same**.

Each node has another two boolean attributes : `isLeaf` and `val`. `isLeaf` is
true if and only if the node is a leaf node. The `val` attribute for a leaf
node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following
example may help you understand the problem better:

Given the `8 x 8` grid below, we want to construct the corresponding quad
tree:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/01/962_grid.png)

It can be divided according to the definition above:

![](https://s3-lc-
upload.s3.amazonaws.com/uploads/2018/02/01/962_grid_divided.png)



The corresponding quad tree should be as following, where each node is
represented as a `(isLeaf, val)` pair.

For the non-leaf nodes, `val` can be arbitrary, so it is represented as `*`.

![](https://s3-lc-
upload.s3.amazonaws.com/uploads/2018/02/01/962_quad_tree.png)

**Note:**

  1. `N` is less than `1000` and guaranteened to be a power of 2.
  2. If you want to know more about the quad tree, you can refer to its [wiki](https://en.wikipedia.org/wiki/Quadtree).


Similar Questions:

"""


"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
