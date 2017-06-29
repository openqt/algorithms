# coding=utf-8
"""
1000-digit Fibonacci number
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""
from __future__ import print_function
from utils import fibonacci


if __name__ == '__main__':
    n = 0
    for i in fibonacci():
        n += 1
        if len(str(i)) >= 1000:
            print(n, i)  # 4782
            break

# The Journey Begins: Progress to Level 1 by solving twenty-five problems
