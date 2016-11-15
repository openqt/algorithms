# coding=utf-8
import unittest


class Solution(unittest.TestCase):
    """
    9. Palindrome Number

    Determine whether an integer is a palindrome. Do this without extra space.

    Some hints:

        Could negative integers be palindromes? (ie, -1)

        If you are thinking of converting the integer to string, note the
        restriction of using extra space.

        You could also try reversing an integer. However, if you have solved
        the problem "Reverse Integer", you know that the reversed integer might
        overflow. How would you handle such case?

        There is a more generic way of solving this problem.
    """

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:  # 负数不是回文数
            return False

        # len = 1  # 找到最高位
        # while x // len >= 10:
        #     len *= 10
        #
        # while x:
        #     if x // len != x % 10:  # high != low
        #         return False
        #
        #     x = (x % len) // 10
        #     len //= 100
        # return True

        n, y = x, 0
        while n:
            y = y * 10 + n % 10
            n //= 10
        return x == y

    def test(self):
        self.assertFalse(self.isPalindrome(10))
        self.assertTrue(self.isPalindrome(1001))
        self.assertFalse(self.isPalindrome(123312))


if __name__ == '__main__':
    unittest.main()
