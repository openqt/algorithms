'''
Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex < 0: return []

        val = [1]
        for i in range(rowIndex):
            val = self._gen(val)
        return val

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
    print s.getRow(5)
    print s.getRow(3)
    print 'PASS'
