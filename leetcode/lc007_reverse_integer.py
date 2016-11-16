import unittest


class Solution(unittest.TestCase):
    """
    7. Reverse Integer

    Reverse digits of an integer.

        Example1: x = 123, return 321
        Example2: x = -123, return -321

    Have you thought about this?

    Here are some good questions to ask before coding. Bonus points for you if
    you have already thought through this!

    If the integer's last digit is 0, what should the output be? ie, cases such
    as 10, 100.

    Did you notice that the reversed integer might overflow? Assume the input
    is a 32-bit integer, then the reverse of 1000000003 overflowself. How
    should you handle such cases?

    For the purpose of this problem, assume that your function returns 0 when
    the reversed integer overflowself.

    Update (2014-11-10):
    Test cases had been added to test the overflow behavior.
    """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        positive = x >= 0
        x = max(x, -x)

        val = 0
        while x:
            val = val * 10 + x % 10
            x //= 10

        if val >= 2147483647:
            return 0

        return val if positive else -val

    def test(self):
        self.assertEqual(self.reverse(0), 0)
        self.assertEqual(self.reverse(123), 321)
        self.assertEqual(self.reverse(-123), -321)
        self.assertEqual(self.reverse(1534236469), 0)
        self.assertEqual(self.reverse(-2147483648), 0)


if __name__ == '__main__':
    unittest.main()
