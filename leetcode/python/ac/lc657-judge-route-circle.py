# coding=utf-8
import unittest

"""657. Judge Route Circle
https://leetcode.com/problems/judge-route-circle/description/

Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to **the
original place**.

The move sequence is represented by a string. And each move is represent by a
character. The valid robot moves are `R` (Right), `L` (Left), `U` (Up) and `D`
(down). The output should be true or false representing whether the robot
makes a circle.

**Example 1:**  

    
    
    **Input:** "UD"
    **Output:** true
    

**Example 2:**  

    
    
    **Input:** "LL"
    **Output:** false


Similar Questions:
  Friend Circles (friend-circles)
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for c in moves:
            if c == "U":
                y += 1
            elif c == "D":
                y -= 1
            elif c == "L":
                x -= 1
            elif c == "R":
                x += 1
            else:
                pass
        return (x, y) == (0, 0)


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.judgeCircle("UD"))
        self.assertFalse(s.judgeCircle("LL"))


if __name__ == "__main__":
    unittest.main()
