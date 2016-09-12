'''
Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n in self.m:
            return self.m[n]
        else:
            steps = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.m[n] = steps
            return steps

    def __init__(self):
        self.m = {0: 1, 1: 1}


if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(3) == 3
    print s.climbStairs(35) == 14930352
    print s.climbStairs(2) == 2
    print 'PASS'
