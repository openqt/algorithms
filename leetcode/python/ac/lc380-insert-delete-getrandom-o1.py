# coding=utf-8
import unittest

"""380. Insert Delete GetRandom O(1)
https://leetcode.com/problems/insert-delete-getrandom-o1/description/

Design a data structure that supports all following operations in _average_
**O(1)** time.

  1. `insert(val)`: Inserts an item val to the set if not already present.
  2. `remove(val)`: Removes an item val from the set if present.
  3. `getRandom`: Returns a random element from current set of elements. 
  Each element must have the **same probability** of being returned.

**Example:**

    
    
    // Init an empty set.
    RandomizedSet randomSet = new RandomizedSet();
    
    // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1);
    
    // Returns false as 2 does not exist in the set.
    randomSet.remove(2);
    
    // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2);
    
    // getRandom should return either 1 or 2 randomly.
    randomSet.getRandom();
    
    // Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1);
    
    // 2 was already in the set, so return false.
    randomSet.insert(2);
    
    // Since 2 is the only number in the set, getRandom always return 2.
    randomSet.getRandom();


Similar Questions:
  Insert Delete GetRandom O(1) - Duplicates allowed (insert-delete-getrandom-o1-duplicates-allowed)
"""

import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = []
        self.field = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.field:
            return False
        self.value.append(val)
        self.field[val] = len(self.value) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.field:
            pos = self.field[val]

            self.value[pos] = self.value[-1]
            self.field[self.value[-1]] = pos

            self.value.pop()
            del self.field[val]  # 必须最后删除以避免pos就是最后一个
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.value:
            return random.choice(self.value)
        return -1


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class T(unittest.TestCase):
    def test(self):
        obj = RandomizedSet()
        self.assertTrue(obj.insert(2))
        self.assertTrue(obj.insert(3))
        self.assertTrue(obj.insert(4))
        self.assertTrue(obj.remove(2))
        # self.assertEqual(obj.getRandom(), -1)


if __name__ == "__main__":
    unittest.main()
