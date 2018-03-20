#!/usr/bin/env python
# coding=utf-8
"""
Passcode derivation
Problem 79

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278, 
they may ask for the 2nd, 3rd, and 5th characters; 
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, 
analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""
from __future__ import print_function


if __name__ == '__main__':
    with open("data/p079_keylog.txt") as f:
        codes = [i.strip() for i in f]
    passcode = set()

    for code in codes:
        for i in code:
            if i not in passcode:
                passcode.add(i)

    print(passcode, len(passcode))
