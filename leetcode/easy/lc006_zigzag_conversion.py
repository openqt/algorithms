'''
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        zigzag = []
        level = num = 0
        while num < len(s):
            level += 1
            if level % 2 == 1:
                o = s[num: num+numRows]
                if len(o) < numRows:
                    o += ' ' * (numRows - len(o))
                zigzag.append(o)
                num += numRows
            elif numRows > 2:
                o = ' ' + s[num: num+numRows-2]
                if len(o) < numRows:
                    o += ' ' * (numRows - len(o))
                zigzag.append(o[::-1])
                num += numRows - 2

        # print zigzag
        val = ''
        for i in range(numRows):
            for j in range(len(zigzag)):
                if zigzag[j][i] != ' ':
                    val += zigzag[j][i]
        return val


if __name__ == '__main__':
    s = Solution()
    assert s.convert('AB', 1) == 'AB'
    assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    print s.convert('ABCDE', 4)
    print 'PASS'
