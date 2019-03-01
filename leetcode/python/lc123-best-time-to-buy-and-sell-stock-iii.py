# coding=utf-8
import unittest

"""123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

Say you have an array for which the _i_ th element is the price of a given
stock on day _i_.

Design an algorithm to find the maximum profit. You may complete at most _two_
transactions.

**Note:  **You may not engage in multiple transactions at the same time (i.e.,
you must sell the stock before you buy again).

**Example 1:**

    
    
    **Input:** [3,3,5,0,0,3,1,4]
    **Output:** 6
    **Explanation:** Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
                  Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

**Example 2:**

    
    
    **Input:** [1,2,3,4,5]
    **Output:** 4
    **Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                  Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.
    

**Example 3:**

    
    
    **Input:** [7,6,4,3,1]
    **Output:** 0
    **Explanation:** In this case, no transaction is done, i.e. max profit = 0.


Similar Questions:
  Best Time to Buy and Sell Stock (best-time-to-buy-and-sell-stock)
  Best Time to Buy and Sell Stock II (best-time-to-buy-and-sell-stock-ii)
  Best Time to Buy and Sell Stock IV (best-time-to-buy-and-sell-stock-iv)
  Maximum Sum of 3 Non-Overlapping Subarrays (maximum-sum-of-3-non-overlapping-subarrays)
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = []
        total, profit = [], 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                pass
            else:
                low.append(prices[i])
                total.append(profit)
                profit = 0
        total.append(profit)
        print(total)
        return sum(sorted(total, reverse=True)[:2])


class T(unittest.TestCase):
    def _test(self):
        s = Solution()
        self.assertEqual(s.maxProfit([]), 0)
        self.assertEqual(s.maxProfit([3,3,5,0,0,3,1,4]), 6)
        self.assertEqual(s.maxProfit([1,2,3,4,5]), 4)
        self.assertEqual(s.maxProfit([7,6,4,3,1]), 0)

    def test2(self):
        s = Solution()
        self.assertEqual(s.maxProfit([1,2,4,2,5,7,2,4,9,0]), 13)

if __name__ == "__main__":
    unittest.main()
