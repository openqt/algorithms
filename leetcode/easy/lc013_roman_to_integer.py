# -*- encoding: utf-8 -*-
'''
Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        D = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        s = s.upper()
        val = 0
        i = 0
        while i < len(s) - 1:
            cur = D[s[i]]
            next = D[s[i+1]]
            if cur >= next:
                val += cur
                i += 1
            else:
                val += next - cur
                i += 2
        if i < len(s): val += D[s[i]]
        return val


if __name__ == '__main__':
    s = Solution()
    print s.romanToInt('I') == 1
    print s.romanToInt('VIII') == 8
    print s.romanToInt('XIV') == 14
    print s.romanToInt('XLV') == 45
    print s.romanToInt('XCIX') == 99
    print s.romanToInt('MCDXXXVII') == 1437
    print 'PASS'
