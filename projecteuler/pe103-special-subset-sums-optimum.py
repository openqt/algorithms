#!/usr/bin/env python
# coding=utf-8

"""103. Special subset sums: optimum
https://projecteuler.net/problem=103

Let S(A) represent the sum of elements in set A of size _n_. We shall call it
a special sum set if for any two non-empty disjoint subsets, B and C, the
following properties are true:

  1. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
  2. If B contains more elements than C then S(B) > S(C).

If S(A) is minimised for a given _n_ , we shall call it an optimum special sum
set. The first five optimum special sum sets are given below.

_n_ = 1: {1}  
 _n_ = 2: {1, 2}  
 _n_ = 3: {2, 3, 4}  
 _n_ = 4: {3, 5, 6, 7}  
 _n_ = 5: {6, 9, 11, 12, 13}

It _seems_ that for a given optimum set, A = { _a_ 1, _a_ 2, ... , _a_ n}, the
next optimum set is of the form B = { _b_ , _a_ 1+ _b_ , _a_ 2+ _b_ , ... ,
_a_ n+ _b_ }, where _b_ is the "middle" element on the previous row.

By applying this "rule" we would expect the optimum set for _n_ = 6 to be A =
{11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum
set, as we have merely applied an algorithm to provide a near optimum set. The
optimum set for _n_ = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and
corresponding set string: 111819202225.

Given that A is an optimum special sum set for _n_ = 7, find its set string.

NOTE: This problem is related to [Problem 105](problem=105) and [Problem
106](problem=106).
"""
