'''
Plus One

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''


class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        val = []
        carry = 1
        for i in digits[::-1]:
            carry += i
            val.append(carry % 10)
            carry /= 10
        if carry > 0:
            val.append(carry)
        return val[::-1]


if __name__ == '__main__':
    s = Solution()
    print s.plusOne([0]) == [1]
    print s.plusOne([9,9,9]) == [1,0,0,0]
    print 'PASS'
