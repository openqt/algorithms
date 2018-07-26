# coding=utf-8
import unittest

"""470. Implement Rand10() Using Rand7()
https://leetcode.com/problems/implement-rand10-using-rand7/description/

Given a function `rand7` which generates a uniform random integer in the range
1 to 7, write a function `rand10` which generates a uniform random integer in
the range 1 to 10.

Do NOT use system's `Math.random()`.



**Example 1:**

    
    
    **Input:** 1
    **Output:** [7]
    

**Example 2:**

    
    
    **Input:** 2
    **Output:** [8,4]
    

**Example 3:**

    
    
    **Input:** 3
    **Output:** [8,1,10]
    



**Note:**

  1. `rand7` is predefined.
  2. Each testcase has one argument: `n`, the number of times that `rand10` is called.



**Follow up:**

  1. What is the [expected value](https://en.wikipedia.org/wiki/Expected_value) for the number of calls to `rand7()` function?
  2. Could you minimize the number of calls to `rand7()`?


Similar Questions:

"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main()
