# coding=utf-8
"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""
from __future__ import print_function


class Solution(object):
    def climbStairs1(self, n, cache=None):
        """
        :type n: int
        :rtype: int
        """
        if cache is None:
            cache = {}
        if n in cache:
            return cache[n]
        if n <= 2:
            return n
        cache[n] = self.climbStairs(n - 1, cache) + \
                   self.climbStairs(n - 2, cache)
        return cache[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [0, 1, 2]
        for i in range(3, n + 1):
            cache.append(cache[i - 1] + cache[i - 2])
        return cache[n]


if __name__ == '__main__':
    so = Solution()
    print(so.climbStairs(3))  # 3
    print(so.climbStairs(35))  # 14930352
