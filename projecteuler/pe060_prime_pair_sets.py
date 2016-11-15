# coding=utf-8
"""
Prime pair sets
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
and concatenating them in any order the result will always be prime. For
example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four
primes, 792, represents the lowest sum for a set of four primes with this
property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
from __future__ import print_function
from pe003_largest_prime_factor import prime_sieve
from pe007_10001st_primes import is_prime
from pe057_square_root_convergents import int_len


def is_concatenating_prime(a, b):
    return is_prime(a * 10 ** int_len(b) + b) and \
           is_prime(b * 10 ** int_len(a) + a)


def _dfs(seq, k, vals):
    if len(vals) >= k:
        yield vals
    else:
        seq = [i for i in seq
               if i > vals[-1] and is_concatenating_prime(i, vals[-1])]
        if len(seq) + len(vals) < k:
            return

        for i in seq:
            for j in _dfs(seq, k, vals + [i]):
                yield j


if __name__ == '__main__':
    seq = [i for i in prime_sieve(10000)]
    for n in seq[:20]:
        for i in _dfs(seq, 5, [n]):
            print(sum(i), i)  # 26033 [13, 5197, 5701, 6733, 8389]
