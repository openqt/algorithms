'''
LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. 
'''


class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LinkedNode:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, pos, node):
        self.count += 1
        if self.count == 1:
            self.tail = node
            self.head = node
        else:  # pos=0
            node.next = self.head
            self.head.pre = node
            self.head = node

        return node

    def remove(self, node):
        self.count -= 1

        if self.count == 0:
            self.head = self.tail = None
        elif node == self.head:
            self.head = node.next
            node.next.pre = None
        elif node == self.tail:
            self.tail = node.pre
            node.pre.next = None
        else:
            node.next.pre = node.pre
            node.pre.next = node.next

        return node

    def length(self):
        return self.count

    def last(self):
        return self.tail

    def show(self):
        p = self.head
        while p:
            print '({},{})'.format(p.key, p.val),
            p = p.next
        print ""


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = LinkedNode()
        self.map = {}

    # @return an integer
    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.cache.remove(node)
            self.cache.add(0, node)
            return node.val

        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.map:
            self.cache.remove(self.map[key])
        else:
            if self.cache.length() >= self.capacity:
                node = self.cache.last()
                self.map.pop(node.key)
                self.cache.remove(node)
        self.map[key] = self.cache.add(0, Node(key, value))

if __name__ == '__main__':
    lru = LRUCache(1)
    lru.set(2, 1)
    lru.get(2)

    for i in range(1, 5):
        lru.set(i, i)
    for i in range(4, 0, -1):
        print lru.get(i)
        lru.cache.show()

    lru.set(5, 5)
    lru.cache.show()
    for i in range(5, 0, -1):
        print lru.get(i)
        lru.cache.show()
