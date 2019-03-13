#!/usr/bin/env python
# coding=utf-8

"""529. 10-substrings
https://projecteuler.net/problem=529

A _10-substring_ of a number is a substring of its digits that sum to 10. For
example, the 10-substrings of the number 3523014 are:

  * **_352_** 3014
  * 3 ** _523_** 014
  * 3 ** _5230_** 14
  * 35 ** _23014_**

A number is called _10-substring-friendly_ if every one of its digits belongs
to a 10-substring. For example, 3523014 is 10-substring-friendly, but 28546 is
not.

Let T(n) be the number of 10-substring-friendly numbers from 1 to 10n
(inclusive).  
For example T(2) = 9 and T(5) = 3492.

Find T(1018) mod 1 000 000 007.
"""
