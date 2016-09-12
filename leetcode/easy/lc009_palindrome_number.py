# coding=utf-8
"""
009. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:

    Could negative integers be palindromes? (ie, -1)

    If you are thinking of converting the integer to string, note the restriction of using extra space.

    You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
    you know that the reversed integer might overflow. How would you handle such case?

    There is a more generic way of solving this problem.
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:  # 负数不是回文数
            return False

        len = 1  # 找到最高位
        while x / len >= 10:
            len *= 10

        while x:
            if x / len != x % 10:  # high != low
                return False

            x = (x % len) / 10
            len /= 100
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(1001)
    print 'PASS'
