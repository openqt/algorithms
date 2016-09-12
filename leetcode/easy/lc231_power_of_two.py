'''
Power of Two

Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo2(self, n):
        if n <= 0: return False
        if n <= 2: return True
        while n > 2:
            if n % 2 == 1: return False
            n /= 2
        return n == 2

    def isPowerOfTwo(self, n):
        return (n > 0) and (n & (n-1) == 0)


if __name__ == '__main__':
    s = Solution()
    print s.isPowerOfTwo(1)
    print s.isPowerOfTwo(64)
    print s.isPowerOfTwo(126)
    print 'PASS'
