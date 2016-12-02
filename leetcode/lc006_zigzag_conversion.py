import unittest


class Solution(unittest.TestCase):
    """6. ZigZag Conversion

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given
    number of rows like this: (you may want to display this pattern in a fixed
    font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a
    number of rows:

        string convert(string text, int nRows);

    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
    """

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = []  # save by column
        _sp = ' '

        col = n = 0
        while n < len(s):
            col += 1
            if col % 2 == 1:
                zigzag.append(s[n: n + numRows].ljust(numRows, _sp))
                n += numRows
            elif numRows > 2:
                t = (_sp + s[n:n + numRows - 2]).ljust(numRows, _sp)
                zigzag.append(t[::-1])
                n += numRows - 2

        val = ''
        for zig in zip(*zigzag):
            val += ''.join(i for i in zig if i != _sp)

        return val

    def test(self):
        self.assertEqual(self.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(self.convert('AB', 1), 'AB')
        self.assertEqual(self.convert('ABC', 2), 'ACB')
        self.assertEqual(self.convert('ABCDE', 4), 'ABCED')


if __name__ == '__main__':
    unittest.main()
