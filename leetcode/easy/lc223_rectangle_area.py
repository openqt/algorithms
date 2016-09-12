# -*- encoding: utf-8 -*-
'''
Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

Credits:
Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.
'''


class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        # if E < C: left = max(A, E)
        # else: left = None
        #
        # if A < G: right = min(C, G)
        # else: left = None
        #
        # if B < H: top = min(D, H)
        # else: left = None
        #
        # if F < D: bottom = max(B, F)
        # else: left = None

        dup = max(min(C, G)-max(A,E), 0) * max(min(D, H)-max(B,F), 0)
        area = (C-A)*(D-B) + (G-E)*(H-F) - dup
        # if left is not None: area -= (right-left)*(top-bottom)
        return area


if __name__ == '__main__':
    s = Solution()
    print s.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45
    print s.computeArea(0, 0, 0, 0, -1, -1, 1, 1) == 4
    print s.computeArea(-2, -2, 2, 2, 3, 3, 4, 4) == 17
    print s.computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16
    print 'PASS'
