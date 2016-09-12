# coding=utf-8
"""
091. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':  # 空或无效
            return 0

        dp = [1, 1]
        for i in range(2, len(s)+1):
            n = 0
            if s[i-1] != '0':  # 前一个不是0，加上前一个的解码方式
                n += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:  # 前两个可以解码，加上
                n += dp[i-2]
            dp.append(n)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    assert s.numDecodings('0') == 0
    assert s.numDecodings('1') == 1
    assert s.numDecodings('00') == 0
    assert s.numDecodings('10') == 1
    assert s.numDecodings('12') == 2
    assert s.numDecodings('27') == 1
    assert s.numDecodings('100') == 0
    assert s.numDecodings('101') == 1
    assert s.numDecodings('110') == 1
    assert s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948") == 589824
    print 'PASS'
