# coding=utf-8
import unittest

"""1000. Minimum Cost to Merge Stones
https://leetcode.com/problems/minimum-cost-to-merge-stones/description/

There are `N` piles of stones arranged in a row.  The `i`-th pile has
`stones[i]` stones.

A _move_ consists of merging **exactly  `K` consecutive** piles into one pile,
and the cost of this move is equal to the total number of stones in these `K`
piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is
impossible, return `-1`.



**Example 1:**

    
    
    **Input:** stones = [3,2,4,1], K = 2
    **Output:** 20
    **Explanation:**
    We start with [3, 2, 4, 1].
    We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
    We merge [4, 1] for a cost of 5, and we are left with [5, 5].
    We merge [5, 5] for a cost of 10, and we are left with [10].
    The total cost was 20, and this is the minimum possible.
    

**Example 2:**

    
    
    **Input:** stones = [3,2,4,1], K = 3
    **Output:** -1
    **Explanation:** After any merge operation, there are 2 piles left, 
    and we can't merge anymore.  So the task is impossible.
    

**Example 3:**

    
    
    **Input:** stones = [3,5,1,2,6], K = 3
    **Output:** 25
    **Explanation:**
    We start with [3, 5, 1, 2, 6].
    We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
    We merge [3, 8, 6] for a cost of 17, and we are left with [17].
    The total cost was 25, and this is the minimum possible.
    



**Note:**

  * `1 <= stones.length <= 30`
  * `2 <= K <= 30`
  * `1 <= stones[i] <= 100`


Similar Questions:
  Burst Balloons (burst-balloons)
"""


class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        # if len(stones) % K + 1 != K:
        #     return -1
        val = 0
        while len(stones) >= K:
            v, pos = self._min_k(stones, K)
            val += v
            stones = stones[:pos] + [v] + stones[pos+K:]
            # print(stones)
        return val if len(stones) == 1 else -1

    def _min_k(self, stones, K):
        val, pos = sum(stones[:K]), 0
        for i in range(1, len(stones)-K+1):
            t = sum(stones[i:i+K])
            if t < val:
                val, pos = t, i
        return val, pos


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.mergeStones([6, 4, 4, 6], 2), 40)
        self.assertEqual(s.mergeStones([3, 2, 4, 1], 2), 20)
        self.assertEqual(s.mergeStones([3, 2, 4, 1], 3), -1)
        self.assertEqual(s.mergeStones([3, 5, 1, 2, 6], 3), 25)


if __name__ == "__main__":
    unittest.main()
