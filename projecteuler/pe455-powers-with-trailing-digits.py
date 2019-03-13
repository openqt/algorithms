#!/usr/bin/env python
# coding=utf-8

"""455. Powers With Trailing Digits
https://projecteuler.net/problem=455

Let f(n) be the largest positive integer x less than 109 such that the last 9
digits of nx form the number _x_ (including leading zeros), or zero if no such
integer exists.

For example:

  * f(4) = 411728896 (4411728896 = ...490 _411728896_ ) 
  * f(10) = 0
  * f(157) = 743757 (157743757 = ...567 _000743757_ )
  * Σf(n), 2 ≤ n ≤ 103 = 442530011399

Find Σf(n), 2 ≤ n ≤ 106.
"""
