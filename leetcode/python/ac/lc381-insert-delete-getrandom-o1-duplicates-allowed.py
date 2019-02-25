# coding=utf-8
import unittest

"""381. Insert Delete GetRandom O(1) - Duplicates allowed
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

Design a data structure that supports all following operations in _average_
**O(1)** time.

**Note: Duplicate elements are allowed.**

  1. `insert(val)`: Inserts an item val to the collection.
  2. `remove(val)`: Removes an item val from the collection if present.
  3. `getRandom`: Returns a random element from current collection of elements. 
  The probability of each element being returned is **linearly related** to the number of same value the collection contains.

**Example:**

    
    
    // Init an empty collection.
    RandomizedCollection collection = new RandomizedCollection();
    
    // Inserts 1 to the collection. Returns true as the collection did not contain 1.
    collection.insert(1);
    
    // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
    collection.insert(1);
    
    // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
    collection.insert(2);
    
    // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
    collection.getRandom();
    
    // Removes 1 from the collection, returns true. Collection now contains [1,2].
    collection.remove(1);
    
    // getRandom should return 1 and 2 both equally likely.
    collection.getRandom();


Similar Questions:
  Insert Delete GetRandom O(1) (insert-delete-getrandom-o1)
"""
import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = []
        self.field = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.value.append(val)
        if val in self.field:
            pos = self.field[val]
            pos.add(len(self.value) - 1)
            return False
        else:
            self.field[val] = {len(self.value) - 1}
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.field:
            pos = self.field[val]
            # 这里已经删除了当前元素
            idx = pos.pop()

            # 如果是最后一项不进行填充，因为前面已经删除了
            if idx < len(self.value)-1:
                # 用最后一个值填充
                self.value[idx] = self.value[-1]
                # 更新索引
                last_pos = self.field[self.value[-1]]
                last_pos.remove(len(self.value)-1)
                last_pos.add(idx)
            # 删除数组最后一项
            self.value.pop()
            # 删除当前索引
            if len(pos) == 0:
                del self.field[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if self.value:
            return random.choice(self.value)
        return -1

    # Your RandomizedCollection object will be instantiated and called as such:
    # obj = RandomizedCollection()
    # param_1 = obj.insert(val)
    # param_2 = obj.remove(val)
    # param_3 = obj.getRandom()

class T(unittest.TestCase):
    def test1(self):
        obj = RandomizedCollection()
        self.assertFalse(obj.remove(3))

        self.assertTrue(obj.insert(1))
        obj.remove(1)
        obj.insert(1)

    def test2(self):
        # ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
        # [[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]
        obj = RandomizedCollection()
        obj.insert(4)
        obj.insert(3)
        obj.insert(4)
        obj.insert(2)
        obj.insert(4)
        obj.remove(4)
        obj.remove(3)
        obj.remove(4)
        obj.remove(4)

    def test3(self):
        # ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
        # [[], [1], [1], [2], [], [1], []]
        obj = RandomizedCollection()
        self.assertTrue(obj.insert(1))
        self.assertEqual(obj.getRandom(), 1)

        self.assertFalse(obj.insert(1))
        self.assertTrue(obj.insert(2))


if __name__ == "__main__":
    unittest.main()
