# coding=utf-8
"""
91. Decode Ways

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
from __future__ import print_function


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        ways = [1, 1]
        for i in range(1, len(s)):
            if s[i] == '0':  # 如果是0， 前面是1，2，取之前解码方式
                if s[i - 1] in ('1', '2'):
                    ways.append(ways[-2])
                else:  # 否则无法解码
                    return 0
            elif (s[i - 1] == '1') or (s[i - 1] == '2' and s[i] <= '6'):
                ways.append(ways[-1] + ways[-2])
            else:  # 需要将相同解码方式记录以备后继处理
                ways.append(ways[-1])
        return ways[-1]


if __name__ == '__main__':
    so = Solution()
    print(so.numDecodings('0'))  # 0
    print(so.numDecodings('10'))  # 1
    print(so.numDecodings('100'))  # 0
    print(so.numDecodings('110'))  # 1
    print(so.numDecodings('12'))  # 2
    print(so.numDecodings('121'))  # 3
    print(so.numDecodings('1212'))  # 5
    print(so.numDecodings('24726'))  # 4
    print(so.numDecodings('47575625458446174945557745813412115112968167865867'
                          '87755257741178599337186486723247528324612117156948'))  # 589824
