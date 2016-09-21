# coding=utf-8
"""
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock
on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
    Input: [7, 1, 5, 3, 6, 4]
    Output: 5

    max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
    than buying price)

Example 2:
    Input: [7, 6, 4, 3, 1]
    Output: 0

    In this case, no transaction is done, i.e. max profit = 0.
"""
from __future__ import print_function


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_val, profit = prices[0], 0
        for i in prices:
            min_val = min(min_val, i)
            profit = max(profit, i - min_val)
        return profit


if __name__ == '__main__':
    so = Solution()
    print(so.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(so.maxProfit([7, 6, 4, 3, 1]))  # 0
    print(so.maxProfit([1, 2]))  # 1
    print(so.maxProfit([2, 1, 4]))  # 3
