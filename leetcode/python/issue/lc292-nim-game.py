# coding=utf-8
import unittest

"""292. Nim Game
https://leetcode.com/problems/nim-game/description/

You are playing the following Nim Game with your friend: There is a heap of
stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the first
turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a
function to determine whether you can win the game given the number of stones
in the heap.

**Example:**

    
    
    **Input:** 4
    **Output:** false 
    **Explanation:** If there are 4 stones in the heap, then you will never win the game;
                 No matter 1, 2, or 3 stones you remove, the last stone will always be 
                 removed by your friend.


Similar Questions:
  Flip Game II (flip-game-ii)
"""


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        self.mem = {}
        return self._sg(n) > 0

    def _sg(self, n):
        if n not in self.mem:
            if n <= 0: return 1
            if n <= 3: return 0
            self.mem[n] = self.canWinNim(n-1) ^ self.canWinNim(n-2) ^ self.canWinNim(n-3)
        return self.mem[n]


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertTrue(s.canWinNim(1))
        self.assertFalse(s.canWinNim(4))


if __name__ == "__main__":
    unittest.main()
