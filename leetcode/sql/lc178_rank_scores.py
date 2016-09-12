# coding=utf-8
"""
178. Rank Scores

Write a SQL query to rank scores. If there is a tie between two scores,
both should have the same ranking.
Note that after a tie, the next ranking number should be the next consecutive integer value.
In other words, there should be no "holes" between ranks.

    +----+-------+
    | Id | Score |
    +----+-------+
    | 1  | 3.50  |
    | 2  | 3.65  |
    | 3  | 4.00  |
    | 4  | 3.85  |
    | 5  | 4.00  |
    | 6  | 3.65  |
    +----+-------+

For example, given the above Scores table, your query should generate the following report (order by highest score):

    +-------+------+
    | Score | Rank |
    +-------+------+
    | 4.00  | 1    |
    | 4.00  | 1    |
    | 3.85  | 2    |
    | 3.65  | 3    |
    | 3.65  | 3    |
    | 3.50  | 4    |
    +-------+------+
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
