#!/usr/bin/env python
# coding=utf-8

"""275. Balanced Sculptures
https://projecteuler.net/problem=275

Let us define a _balanced sculpture_ of order  n as follows:

  * A polyomino made up of n+1 tiles known as the _blocks_ ( n tiles)  
and the _plinth_ (remaining tile);

  * the plinth has its centre at position (x = 0, y = 0);
  * the blocks have y-coordinates greater than zero (so the plinth is the unique lowest tile);
  * the centre of mass of all the blocks, combined, has x-coordinate equal to zero.

When counting the sculptures, any arrangements which are simply reflections
about the y-axis, are _not_ counted as distinct. For example, the 18 balanced
sculptures of order 6 are shown below; note that each pair of mirror images
(about the  y-axis) is counted as one sculpture:

There are 964 balanced sculptures of order 10 and 360505 of order 15.  
How many balanced sculptures are there of order 18?
"""
