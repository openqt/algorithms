#!/usr/bin/env python
# coding=utf-8

"""149. Searching for a maximum-sum subsequence
https://projecteuler.net/problem=149

Looking at the table below, it is easy to verify that the maximum possible sum
of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-
diagonal) is 16 (= 8 + 7 + 1).

Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of
what is known as a "Lagged Fibonacci Generator":

For 1 ≤ _k_ ≤ 55, _s_ _k_ = [100003 − 200003 _k_ \+ 300007 _k_ 3] (modulo
1000000) − 500000.  
For 56 ≤ _k_ ≤ 4000000, _s_ _k_ = [ _s_ _k−24_ \+ _s_ _k−55_ \+ 1000000]
(modulo 1000000) − 500000.

Thus, _s_ 10 = −393027 and _s_ 100 = 86613.

The terms of _s_ are then arranged in a 2000×2000 table, using the first 2000
numbers to fill the first row (sequentially), the next 2000 numbers to fill
the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any
direction (horizontal, vertical, diagonal or anti-diagonal).
"""
