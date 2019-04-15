# lc218 hte skyline
def skyline():
    pass

# lc973 k closest points

# lc587 erect the fence

# RB-Tree, AVL Tree, AA Tree, Splay Tree, skip list

# interval tree, quad tree, oct tree

# interpolation search
from itertools import count

class Node:
    def __init__(self, v):
        self.val = v
        self.left = self.right = None


def binary_tree(seq):
    def build(node, val):
        if node is None: return Node(val)
        if val <= node.val:
            node.left = build(node.left, val)
        else:
            node.right = build(node.right, val)
        return node

    node = None
    for i in seq:
        node = build(node, i)
    return node


def preorder(node, deep=0):
    if node:
        print(node.val, ":", deep)
        preorder(node.left, deep + 1)
        preorder(node.right, deep + 1)


def partation(seq):
    pi, seq = seq[0], seq[1:]
    lo, hi = [], []
    for i in seq:
        if i <= pi:
            lo.append(i)
        else:
            hi.append(i)
    return lo, pi, hi


def select(seq, k):
    lo, pi, hi = partation(seq)
    m = len(lo)
    if m == k:
        return lo
    if m < k:
        return lo + [pi] + select(hi, k - m - 1)
    return select(lo, k)


def quicksort(seq):
    if len(seq) <= 1: return seq
    lo, pi, hi = partation(seq)
    return quicksort(lo) + [pi] + quicksort(hi)


def mergesort(seq) -> list:
    m = len(seq) // 2
    lft, rgt = seq[:m], seq[m:]
    if lft > 1: lft = mergesort(lft)
    if rgt > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] > rgt[-1]:
            res.append(lft.pop)
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == '__main__':
    from random import randrange
    from heapq import merge

    preorder(binary_tree([4, 3, 2, 1, 5, 6, 7, 8]))

    seq = [randrange(100) for i in range(20)]
    print('seq', seq)
    print('sorted', sorted(seq))
    print(select(seq, 5))
    print(quicksort(seq.copy()))
