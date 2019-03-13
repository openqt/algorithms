#!/usr/bin/env python
# coding=utf-8

"""261. Pivotal Square Sums
https://projecteuler.net/problem=261

Let us call a positive integer k a square-pivot, if there is a pair of
integers m > 0 and n ≥ k, such that the sum of the (m+1) consecutive squares
up to k equals the sum of the m consecutive squares from (n+1) on:

(k-m)2 \+ ... + k2 = (n+1)2 \+ ... + (n+m)2.

Some small square-pivots are

  * **4** : 32 \+ **4** 2 = 52
  * **21** : 202 \+ **21** 2 = 292
  * **24** : 212 \+ 222 \+ 232 \+ **24** 2 = 252 \+ 262 \+ 272
  * **110** : 1082 \+ 1092 \+ **110** 2 = 1332 \+ 1342

Find the sum of all **distinct** square-pivots ≤ 10 10.
"""
