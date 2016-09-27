# coding=utf-8
"""
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from __future__ import print_function


def alphabetical_value(s):
    return sum(ord(i) + 1 for i in s) - (ord('A') * len(s))


if __name__ == '__main__':
    names = None
    with open('data/p022_names.txt') as f:
        names = sorted([i.strip('"') for i in f.read().split(',')])

    total = 0
    for n, i in enumerate(names, 1):
        total += alphabetical_value(i) * n
    print(total)
