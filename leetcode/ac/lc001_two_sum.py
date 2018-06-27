import unittest


class Solution(unittest.TestCase):
    """1. Two Sum

    Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    You may assume that each input would have exactly one solution.

    Example:
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

    UPDATE (2016/2/13):
    The return format had been changed to zero-based indices. Please read the
    above updated description carefully.
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for n, i in enumerate(nums):
            cache.setdefault(i, []).append(n)

        for i in nums:
            j = target - i
            if j == i:
                if len(cache[i]) > 1:
                    return [cache[i][0], cache[i][1]]
            elif j in cache:
                return [cache[i][0], cache[j][0]]
        return None

    def test(self):
        self.assertEqual(self.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.twoSum([0, 4, 3, 0], 0), [0, 3])
        self.assertEqual(self.twoSum([2, 7, 11, 15], 9), [0, 1])


if __name__ == '__main__':
    unittest.main()
