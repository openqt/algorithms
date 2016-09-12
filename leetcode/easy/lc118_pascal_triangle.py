'''
Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows <= 0: return []

        tri = [[1]]
        for i in range(numRows-1):
            tri.append(self._gen(tri[-1]))
        return tri

    def _gen(self, data):
        val = [1]
        a = data[0]
        for i in data[1:]:
            val.append(a+i)
            a = i
        val.append(1)
        return val


if __name__ == '__main__':
    s = Solution()
    print s.generate(5)
    print 'PASS'
