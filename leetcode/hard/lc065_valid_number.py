# coding=utf-8
"""
065. Valid Number

Validate if a given string is numeric.

Some examples:
    "0" => true
    " 0.1 " => true
    "abc" => false
    "1 a" => false
    "2e10" => true

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated.
If you still see your function signature accepts a const char * argument,
please click the reload button to reset your code definition.
"""


class Solution(object):

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        dot = False
        exp = False
        num_dot_front = False
        num_dot_end = False
        num_exp_end = False
        i = 0
        while self.is_space(s, i):
            i += 1

        if self.is_sign(s, i):
            i += 1

        while self.is_digit(s, i):
            num_dot_front = True
            i += 1

        if i < len(s) and s[i] in ('.') and not dot:
            dot = True
            i += 1

        while self.is_digit(s, i):
            num_dot_end = True
            i += 1

        if i < len(s) and s[i] in ('e', 'E') and not exp:
            i += 1
            if self.is_sign(s, i):
                i += 1

            if i >= len(s) or not self.is_digit(s, i):
                return False
            exp = True

        while self.is_digit(s, i):
            num_exp_end = True
            i += 1

        while self.is_space(s, i):
            i += 1

        if dot and not num_dot_front and not num_dot_end:
            return False
        if exp and not num_exp_end:
            return False
        return (num_dot_front or num_dot_end) and i >= len(s)

    def is_space(self, s, i):
        return i < len(s) and s[i] == ' '

    def is_sign(self, s, i):
        return i < len(s) and s[i] in ('+', '-')

    def is_digit(self, s, i):
        return 0 <= i < len(s) and '0' <= s[i] <= '9'

    def isNumber1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False


if __name__ == '__main__':
    s = Solution()
    assert s.isNumber('0')
    assert s.isNumber(' 0.1')
    assert not s.isNumber('abc')
    assert not s.isNumber('1 a')
    assert s.isNumber('2e10')
    assert s.isNumber('0')
    assert not s.isNumber(' e')
    assert not s.isNumber('.')
    assert not s.isNumber('  ')
    assert s.isNumber('.1')
    assert not s.isNumber('0e')
    assert s.isNumber('3.')
    assert s.isNumber('0e1')
    assert s.isNumber('.2e81')
    assert s.isNumber(' 005047e+6')

    print 'PASS'
