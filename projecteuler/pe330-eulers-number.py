#!/usr/bin/env python
# coding=utf-8

"""330. Euler's Number
https://projecteuler.net/problem=330

An infinite sequence of real numbers

a

(

n

) is defined for all integers

n

as follows: $$a(n) = \begin{cases} 1 & n \lt 0\\\ \sum \limits_{i =
1}^{\infty}{\dfrac{a(n - i)}{i!}} & n \ge 0 \end{cases}$$

For example,  

a(1) =  |  | + |  | + |  | \+ ... = 2e − 3  
---|---|---|---|---|---|---  
  
with e = 2.7182818... being Euler's constant.

It can be shown that a(n) is of the form  |  | for integers A(n) and B(n).  
---|---|---  
For example a(10) =  | | 328161643 e − 652694486  
---  
10!  
.  
  
Find A(109) + B(109) and give your answer mod 77 777 777.
"""
