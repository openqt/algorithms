# coding=utf-8
import unittest

"""739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/description/

Given a list of daily `temperatures`, produce a list that, for each day in the
input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put `0`
instead.

For example, given the list `temperatures = [73, 74, 75, 71, 69, 72, 76, 73]`,
your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.

**Note:** The length of `temperatures` will be in the range `[1, 30000]`. Each
temperature will be an integer in the range `[30, 100]`.


Similar Questions:
  Next Greater Element I (next-greater-element-i)
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        val = [0] * len(temperatures)
        stack = []
        for n in range(len(temperatures)):
            while stack and temperatures[n] > stack[-1][0]:
                t = stack.pop()
                val[t[1]] = n - t[1]

            stack.append((temperatures[n], n))  # (temperature, position) pair
        return val


class T(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(s.dailyTemperatures([68, 69, 71, 70, 69, 72, 69, 68, 70]), [1, 1, 3, 2, 1, 0, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()
