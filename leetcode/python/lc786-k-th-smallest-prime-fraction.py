# coding=utf-8
import unittest

"""786. K-th Smallest Prime Fraction
https://leetcode.com/problems/k-th-smallest-prime-fraction/description/

A sorted list `A` contains 1, plus some number of primes.  Then, for every p <
q in the list, we consider the fraction p/q.

What is the `K`-th smallest fraction considered?  Return your answer as an
array of ints, where `answer[0] = p` and `answer[1] = q`.

    
    
    **Examples:**
    **Input:** A = [1, 2, 3, 5], K = 3
    **Output:** [2, 5]
    **Explanation:**
    The fractions to be considered in sorted order are:
    1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
    The third fraction is 2/5.
    
    **Input:** A = [1, 7], K = 1
    **Output:** [1, 7]
    

**Note:**

  * `A` will have length between `2` and `2000`.
  * Each `A[i]` will be between `1` and `30000`.
  * `K` will be between `1` and `A.length * (A.length - 1) / 2`.


Similar Questions:
  Kth Smallest Element in a Sorted Matrix (kth-smallest-element-in-a-sorted-matrix)
  Kth Smallest Number in Multiplication Table (kth-smallest-number-in-multiplication-table)
  Find K-th Smallest Pair Distance (find-k-th-smallest-pair-distance)
"""


class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
