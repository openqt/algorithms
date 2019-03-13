#!/usr/bin/env python
# coding=utf-8

"""137. Fibonacci golden nuggets
https://projecteuler.net/problem=137

Consider the infinite polynomial series AF( _x_ ) = _x_ F1 \+ _x_ 2F2 \+ _x_
3F3 \+ ..., where F _k_ is the _k_ th term in the Fibonacci sequence: 1, 1, 2,
3, 5, 8, ... ; that is, F _k_ = F _k_ −1 \+ F _k_ −2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of _x_ for which A F( _x_ )
is a positive integer.

Surprisingly AF(1/2) |  =  | (1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3 +
(1/2)5.5 + ...  
---|---|---  
|  =  | 1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...  
|  =  | 2  
  
The corresponding values of _x_ for the first five natural numbers are shown
below.

**_x_**|  **A F( _x_ )**  
---|---  
√2−1| 1  
1/2| 2  
(√13−2)/3| 3  
(√89−5)/8| 4  
(√34−3)/5| 5  
  
We shall call AF( _x_ ) a golden nugget if _x_ is rational, because they
become increasingly rarer; for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.
"""
