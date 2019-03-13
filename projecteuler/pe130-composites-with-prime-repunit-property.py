#!/usr/bin/env python
# coding=utf-8

"""130. Composites with prime repunit property
https://projecteuler.net/problem=130

A number consisting entirely of ones is called a repunit. We shall define R(
_k_ ) to be a repunit of length _k_ ; for example, R(6) = 111111.

Given that _n_ is a positive integer and GCD( _n_ , 10) = 1, it can be shown
that there always exists a value, _k_ , for which R( _k_ ) is divisible by _n_
, and let A( _n_ ) be the least such value of _k_ ; for example, A(7) = 6 and
A(41) = 5.

You are given that for all primes, _p_ > 5, that _p_ − 1 is divisible by A(
_p_ ). For example, when _p_ = 41, A(41) = 5, and 40 is divisible by 5.

However, there are rare composite values for which this is also true; the
first five examples being 91, 259, 451, 481, and 703.

Find the sum of the first twenty-five composite values of _n_ for which  
GCD( _n_ , 10) = 1 and _n_ − 1 is divisible by A( _n_ ).
"""
