#!/usr/bin/env python
# coding=utf-8

"""82. Path sum: three ways
https://projecteuler.net/problem=82

NOTE: This problem is a more challenging version of [Problem 81](problem=81).

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in
the left column and finishing in any cell in the right column, and only moving
up, down, and right, is indicated in red and bold; the sum is equal to 994.

$$ \begin{pmatrix} 131 & 673 & \color{red}{234} & \color{red}{103} &
\color{red}{18}\\\ \color{red}{201} & \color{red}{96} & \color{red}{342} & 965
& 150\\\ 630 & 803 & 746 & 422 & 111\\\ 537 & 699 & 497 & 121 & 956\\\ 805 &
732 & 524 & 37 & 331 \end{pmatrix} $$

Find the minimal path sum, in [matrix.txt](project/resources/p082_matrix.txt)
(right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the left column to the right column.
"""
