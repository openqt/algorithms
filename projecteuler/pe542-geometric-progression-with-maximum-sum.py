#!/usr/bin/env python
# coding=utf-8

"""542. Geometric Progression with Maximum Sum
https://projecteuler.net/problem=542

Let S(k) be the sum of three or more distinct positive integers having the
following properties:

  * No value exceeds k.
  * The values form a **geometric progression**.
  * The sum is maximal.

S(4) = 4 + 2 + 1 = 7  
S(10) = 9 + 6 + 4 = 19  
S(12) = 12 + 6 + 3 = 21  
S(1000) = 1000 + 900 + 810 + 729 = 3439

Let $T(n) = \sum_{k=4}^n (-1)^k S(k)$.  
T(1000) = 2268

Find T(1017).
"""
