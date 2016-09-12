'''
Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution:

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0
        max = 0
        for f in points:
            d = {}
            dup = 0
            for p in points:
                if p.x == f.x and p.y == f.y:
                    dup += 1
                else:
                    if p.x == f.x:
                        rate = 0xFFFF
                    else:
                        rate = float(p.y - f.y) / (p.x - f.x)
                    d[rate] = d.setdefault(rate, 0) + 1
            if d:
                m = sorted(d.values(), reverse=True)[0]
            else:
                m = 0
            if m + dup > max:
                max = m + dup
        return max
