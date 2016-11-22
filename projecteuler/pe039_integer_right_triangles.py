# coding=utf-8
"""
Integer right triangles
Problem 39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from __future__ import print_function
from pe009_special_pythagorean_triplet import pythagorean_triplet

# def right_triangle_sides(perimeter):
#     sides = []
#     for a in range(1, perimeter // 3):
#         for b in range(a, perimeter):
#             c = perimeter - a - b
#             if c > a and c > b:
#                 if c ** 2 == a ** 2 + b ** 2:
#                     sides.append((a, b, c))
#     return sides


if __name__ == '__main__':
    n = sides = 0
    for i in range(1001):
        # t = len(right_triangle_sides(i))
        total = sum(1 for _ in pythagorean_triplet(i))
        if total > sides:
            sides = total
            n = i
    print(n)  # 840
