# coding=utf-8
import unittest

"""Knight Probability in Chessboard
https://leetcode.com/problems/knight-probability-in-chessboard/description/

<p>
On an <code>N</code>x<code>N</code> chessboard, a knight starts at the <code>r</code>-th row and <code>c</code>-th column and attempts to make exactly <code>K</code> moves.  The rows and columns are 0 indexed, so the top-left square is <code>(0, 0)</code>, and the bottom-right square is <code>(N-1, N-1)</code>.
</p>

<p>
A chess knight has 8 possible moves it can make, as illustrated below.  Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
</p>

<img src="/static/images/problemset/knight.png" style="width:200px; height:200px"></img>

<p>
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
</p>

<p>
The knight continues moving until it has made exactly <code>K</code> moves or has moved off the chessboard.  Return the probability that the knight remains on the board after it has stopped moving.
</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 3, 2, 0, 0
<b>Output:</b> 0.0625
<b>Explanation:</b> There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
</pre>
</p>

<p><b>Note:</b><br />
<li><code>N</code> will be between 1 and 25.</li>
<li><code>K</code> will be between 0 and 100.</li>
<li>The knight always initially starts on the board.</li>
</p>
"""


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
