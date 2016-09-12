# coding=utf-8
"""
031. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
"""


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 从后往前找到升序的起点
        for n in range(len(nums)-1, 0, -1):
            if nums[n-1] < nums[n]:
                # 找到比起点大的元素，因为升序排列所以第一找到的就是最小的
                val = nums[n - 1]
                for m in range(len(nums)-1, n-1, -1):
                    if nums[m] > val:
                        nums[n-1], nums[m] = nums[m], nums[n-1]
                        break

                # 降序起点后的序列
                i, j = n, len(nums)-1
                while i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1; j -= 1
                return
        nums.reverse()



if __name__ == '__main__':
    s = Solution()

    nums = [1, 2]
    s.nextPermutation(nums)
    print nums
    assert nums == [2, 1]

    nums = [1, 3, 2]
    s.nextPermutation(nums)
    print nums
    assert nums == [2, 1, 3]

    nums = [1, 2, 3]
    s.nextPermutation(nums)
    print nums
    assert nums == [1, 3, 2]

    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print nums
    assert nums == [1, 2, 3]

    nums = [1, 1, 5]
    s.nextPermutation(nums)
    print nums
    assert nums == [1, 5, 1]

    nums = [5, 1, 1]
    s.nextPermutation(nums)
    print nums
    assert nums == [1, 1, 5]

    print 'PASS'
