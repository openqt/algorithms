import unittest

INT_MAX = 2147483647
INT_MIN = -2147483648


class Solution(unittest.TestCase):
    """
    String to Integer (atoi)

    Implement atoi to convert a string to an integer.

    Hint: Carefully consider all possible input cases. If you want a challenge,
    please do not see below and ask yourself what are the possible input cases.

    Notes: It is intended for this problem to be specified vaguely (ie, no
    given input specs). You are responsible to gather all the input
    requirements up front.

    Update (2015-02-10):
    The signature of the C++ function had been updated. If you still see your
    function signature accepts a const char * argument, please click the reload
    button  to reset your code definition.

    Requirements for atoi:
    The function first discards as many whitespace characters as necessary
    until the first non-whitespace character is found. Then, starting from this
    character, takes an optional initial plus or minus sign followed by as many
    numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the
    integral number, which are ignored and have no effect on the behavior of
    this function.

    If the first sequence of non-whitespace characters in str is not a valid
    integral number, or if no such sequence exists because either str is empty
    or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned. If the
    correct value is out of the range of representable values, INT_MAX
    (2147483647) or INT_MIN (-2147483648) is returned.
    """

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        p = 0
        while str[p] == ' ':  # left strip
            p += 1

        positive = True  # sign
        if str[p] in ('+', '-'):
            positive = (str[p] == '+')
            p += 1

        val = 0
        while p < len(str) and '0' <= str[p] <= '9':
            val = val * 10 + (ord(str[p]) - ord('0'))
            p += 1

        val = val if positive else -val

        if val > INT_MAX:
            return INT_MAX

        if val < INT_MIN:
            return INT_MIN

        return val

    def test(self):
        self.assertEqual(self.myAtoi(''), 0)
        self.assertEqual(self.myAtoi('+456.2'), 456)
        self.assertEqual(self.myAtoi('    -00134'), -134)
        self.assertEqual(self.myAtoi('2147483648'), 2147483647)


if __name__ == '__main__':
    unittest.main()
