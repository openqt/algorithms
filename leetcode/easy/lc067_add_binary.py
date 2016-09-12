'''
Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        val = ''
        carry = 0
        a = a[::-1]; b = b[::-1]
        for i in range(max(len(a), len(b))):
            if i < len(a): carry += ord(a[i]) - ord('0')
            if i < len(b): carry += ord(b[i]) - ord('0')
            val += str(carry % 2)
            carry /= 2
        if carry > 0: val += str(carry)
        return val[::-1]


if __name__ == '__main__':
    s = Solution()
    print s.addBinary('11', '1') == '100'
    print s.addBinary('1', '111') == '1000'
    print s.addBinary('1010', '1011') == '10101'
    print 'PASS'
