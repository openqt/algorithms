'''
Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if n <= 0: return 0
        val = 0
        five = 5
        while n/five > 0:
            val += n/five
            five *= 5
        return val


if __name__ == '__main__':
    s = Solution()
    print s.trailingZeroes(30)
    print s.trailingZeroes(200)
    print 'PASS'
