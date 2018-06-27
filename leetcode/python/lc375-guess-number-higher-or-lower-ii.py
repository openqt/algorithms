# coding=utf-8
import unittest

"""375. Guess Number Higher or Lower II
https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/

<p>We are playing the Guess Game. The game is as follows:<p> 

<p>I pick a number from <strong>1</strong> to <strong>n</strong>. You have to guess which number I picked.</p>

<p>Every time you guess wrong, I'll tell you whether the number I picked is higher or lower. </p>

<p>However, when you guess a particular number x,  and you guess wrong, you pay <b>$x</b>. You win the game when you guess the number I picked.</p>

<p>
<b>Example:</b>
<pre>
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
</pre>
</p>

<p>Given a particular <strong>n &ge; 1</strong>, find out how much money you need to have to guarantee a <b>win</b>.</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/agave/">@agave</a> and <a href="https://leetcode.com/stefanpochmann/">@StefanPochmann</a> for adding this problem and creating all test cases.</p>
"""


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
