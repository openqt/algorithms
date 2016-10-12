# coding=utf-8
"""
Coded triangle numbers
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""
from __future__ import print_function
from e0022_names_scores import read_words, alphabetical_value


def triangle_number(stop=-1):
    n = 1
    while stop != 0:
        yield n * (n + 1) / 2
        n += 1

        stop -= 1


if __name__ == '__main__':
    words = read_words('data/p042_words.txt')

    for i in triangle_number(10):
        print(i,)

    print(alphabetical_value('SKY'))
