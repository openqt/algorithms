# coding=utf-8
"""
Maximum path sum II
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and
'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether!
If you could check one trillion (1012) routes every second it would take over
twenty billion years to check them all. There is an efficient algorithm to
solve it. ;o)
"""
from __future__ import print_function
from e0018_maximum_path_sum_i import merge_triangle_down_by_max


def read_triangle_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
           data.append(map(int, line.split()))
    return data


if __name__ == '__main__':
    data = read_triangle_data('data/p067_triangle.txt')

    vals = data[0]
    for i in range(1, len(data)):
        vals = merge_triangle_down_by_max(vals, data[i])

    print(max(vals))  # 7273
