#!/usr/bin/env python
# coding=utf-8

"""539. Odd elimination
https://projecteuler.net/problem=539

Start from an ordered list of all integers from 1 to n. Going from left to
right, remove the first number and every other number afterward until the end
of the list. Repeat the procedure from right to left, removing the right most
number and every other number from the numbers left. Continue removing every
other numbers, alternating left to right and right to left, until a single
number remains.

Starting with n = 9, we have:  
 _1_ 2 _3_ 4 _5_ 6 _7_ 8 _9_  
2 _4_ 6 _8_  
 _2_ 6  
6

Let  P(n) be the last number left starting with a list of length n.  
Let $\displaystyle S(n) = \sum_{k=1}^n P(k)$.  
You are given P(1)=1, P(9) = 6, P(1000)=510, S(1000)=268271.

Find S(1018) mod 987654321.
"""
