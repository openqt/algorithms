#!/usr/bin/env python
# coding=utf-8

"""122. Efficient exponentiation
https://projecteuler.net/problem=122

The most naive way of computing _n_ 15 requires fourteen multiplications:

_n_ × _n_ × ... × _n_ = _n_ 15

But using a "binary" method you can compute it in six multiplications:

_n_ × _n_ = _n_ 2  
 _n_ 2 × _n_ 2 = _n_ 4  
 _n_ 4 × _n_ 4 = _n_ 8  
 _n_ 8 × _n_ 4 = _n_ 12  
 _n_ 12 × _n_ 2 = _n_ 14  
 _n_ 14 × _n_ = _n_ 15

However it is yet possible to compute it in only five multiplications:

_n_ × _n_ = _n_ 2  
 _n_ 2 × _n_ = _n_ 3  
 _n_ 3 × _n_ 3 = _n_ 6  
 _n_ 6 × _n_ 6 = _n_ 12  
 _n_ 12 × _n_ 3 = _n_ 15

We shall define m( _k_ ) to be the minimum number of multiplications to
compute _n_ _k_ ; for example m(15) = 5.

For 1 ≤ _k_ ≤ 200, find  ∑ m( _k_ ).
"""
