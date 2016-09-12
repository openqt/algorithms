'''
Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        ret = '1'
        for i in range(2, n+1):
            ret = self.say(ret)
        print '> ', ret
        return ret

    def say(self, s):
        ret = ''
        c = s[0]; n = 0
        for i in s:
            if i == c:
                n += 1
            else:
                ret += str(n) + c
                c = i; n = 1
        ret += str(n) + c
        return ret


if __name__ == '__main__':
    s = Solution()
    assert s.countAndSay(1) == '1'
    assert s.countAndSay(2) == '11'
    assert s.countAndSay(4) == '1211'
    assert s.countAndSay(5) == '111221'
    print 'PASS'
