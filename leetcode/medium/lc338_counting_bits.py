# coding=utf-8
"""
338. Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

Hint:

You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to generate new range from previous.
Or does the odd/even status of the number help you in calculating the number of 1s?
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    @print_result
    def countBits(self, num):
        """
        O(n)解法
        :type num: int
        :rtype: List[int]
        """
        bits = [0, ]
        for i in range(1, num+1):
            bits.append(bits[i & (i-1)] + 1)
        return bits

    def countBits1(self, num):
        """
        原始解法
        :type num: int
        :rtype: List[int]
        """
        bits = []
        for i in range(num+1):
            bits.append(self.count(i))
        return bits

    def count(self, n):
        c = 0
        while n > 0:
            n &= n-1
            c += 1
        return c

if __name__ == '__main__':
    s = Solution()
    assert s.countBits(5) == [0,1,1,2,1,2]
    print 'PASS'
