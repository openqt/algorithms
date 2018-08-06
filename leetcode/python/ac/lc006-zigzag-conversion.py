# coding=utf-8
import unittest

"""6. ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/description/

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)

    
    
    P   A   H   N
    A P L S I I G
    Y   I   R
    

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number
of rows:

    
    
    string convert(string s, int numRows);

**Example 1:**

    
    
    **Input:** s =  "PAYPALISHIRING", numRows = 3
    **Output:**  "PAHNAPLSIIGYIR"
    

**Example 2:**

    
    
    **Input:** s =  "PAYPALISHIRING", numRows = 4
    **Output:**  "PINALSIGYAHRPI"
    **Explanation:**
    
    P     I    N
    A   L S  I G
    Y A   H R
    P     I


Similar Questions:

"""


class Solution(unittest.TestCase):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        def calc_pos(n):
            base = numRows * 2 - 2
            col = int(n / base) * (numRows - 1)
            row = int(n % base)
            if row >= numRows:
                col += row - numRows + 1
                row = numRows - (row - numRows + 1) - 1
            return row, col

        if numRows <= 1:
            return s

        grid = [[''] * len(s) for _ in range(numRows)]
        for n, i in enumerate(s):
            r, c = calc_pos(n)
            grid[r][c] = i

        s = "".join("".join(i) for i in grid)
        return s

    def test(self):
        self.assertEqual(self.convert("PAYPALISHIRING", 1), "PAYPALISHIRING")
        self.assertEqual(self.convert("PAYPALISHIRING", 2), "PYAIHRNAPLSIIG")
        self.assertEqual(self.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(self.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")


if __name__ == "__main__":
    unittest.main()
