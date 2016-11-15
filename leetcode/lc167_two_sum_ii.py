import unittest


class Solution(unittest.TestCase):
    """
    167. Two Sum II - Input array is sorted

    Given an array of integers that is already sorted in ascending order, find
    two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they
    add up to the target, where index1 must be less than index2. Please note
    that your returned answers (both index1 and index2) are not zero-based.

    You may assume that each input would have exactly one solution.

        Input: numbers={2, 7, 11, 15}, target=9
        Output: index1=1, index2=2
    """

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for n, i in enumerate(numbers, 1):
            cache.setdefault(i, []).append(n)

        for i in numbers:
            j = target - i
            if j == i:
                if len(cache[i]) > 1:
                    return [cache[i][0], cache[i][1]]
            elif j in cache:
                return [cache[i][0], cache[j][0]]
        return None

    def test(self):
        self.assertEqual(self.twoSum([2, 7, 11, 15], 9), [1, 2])


if __name__ == '__main__':
    unittest.main()
