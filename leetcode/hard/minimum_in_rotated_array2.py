'''
Find Minimum in Rotated Sorted Array II

    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
'''


class Solution:

    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        pre = num[0]
        for i in num[1:]:
            if i < pre:
                return i
            else:
                pre = i
        return num[0]

if __name__ == '__main__':
    s = Solution()
    assert s.findMin([5, 5, 6, 6, 0, 1, 2]) == 0
    print 'PASS'
