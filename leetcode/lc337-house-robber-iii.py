# coding=utf-8
import unittest

"""House Robber III
https://leetcode.com/problems/house-robber-iii/description/

<p>
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
</p>

<p>
Determine the maximum amount of money the thief can rob tonight without alerting the police.
</p>

<p><b>Example 1:</b><br />
<pre>
     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1</font>
</pre>
Maximum amount of money the thief can rob = <font color="red">3</font> + <font color="red">3</font> + <font color="red">1</font> = <b>7</b>.
</p>

<p><b>Example 2:</b><br />
<pre>
     3
    / \
   <font color="red">4</font>   <font color="red">5</font>
  / \   \ 
 1   3   1
</pre>
Maximum amount of money the thief can rob = <font color="red">4</font> + <font color="red">5</font> = <b>9</b>.
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p>
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
