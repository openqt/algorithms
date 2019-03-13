#!/usr/bin/env python
# coding=utf-8

"""140. Modified Fibonacci golden nuggets
https://projecteuler.net/problem=140

Consider the infinite polynomial series AG( _x_ ) = _x_ G1 \+ _x_ 2G2 \+ _x_
3G3 \+ ..., where G _k_ is the _k_ th term of the second order recurrence
relation G _k_ = G _k_ −1 \+ G _k_ −2, G1 = 1 and G2 = 4; that is, 1, 4, 5, 9,
14, 23, ... .

For this problem we shall be concerned with values of _x_ for which A G( _x_ )
is a positive integer.

The corresponding values of _x_ for the first five natural numbers are shown
below.

**_x_**|  **A G( _x_ )**  
---|---  
(√5−1)/4| 1  
2/5| 2  
(√22−2)/6| 3  
(√137−5)/14| 4  
1/2| 5  
  
We shall call AG( _x_ ) a golden nugget if _x_ is rational, because they
become increasingly rarer; for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.
"""
