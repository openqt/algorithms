# coding=utf-8
"""
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773,
and 56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
"""
from __future__ import print_function
from pe003_largest_prime_factor import prime_sieve
from pe049_prime_permutations import seq_int


def combinations(seq, k):
    """combinations by lexicographic order

    :param seq: choices
    :param k: K
    :return: next combination
    """
    def _inner_dfs(seq, k, vals):
        if len(seq) + len(vals) < k:
            return

        if len(vals) >= k:  # got one
            yield vals
        else:
            for i in range(len(seq)):
                for j in _inner_dfs(seq[i + 1:], k, vals + [seq[i]]):
                    yield j

    # here we added the extra parameter
    for i in _inner_dfs(seq, k, []):
        yield i


def mask_same_digits(n, count=2):
    """mask same digit combinations by '*'

    :param n: the number
    :param count: least same digits
    :return: mask list
    """
    def _same_digits(seq, count):
        m = {}
        for pos, val in enumerate(seq):  # inverted index
            m.setdefault(val, []).append(pos)

        for val, pos in m.items():  # multi pos(es)
            if len(pos) >= count:
                yield pos

    def _mask(seq, mask, sign='*'):
        for i in mask:
            seq[i] = sign
        return ''.join(map(str, seq))

    seq = seq_int(n)
    for pos in _same_digits(seq, count):
        for mask in combinations(pos, count):  # all possible combinations
            yield _mask(seq[:], mask)


# def combine(self, NN, K):
#     """Iterative 8-line solution using C(n, k) = C(n-1, k) + C(n-1, k-1)
#
#     https://discuss.leetcode.com/topic/40827/iterative-8-line-solution-using-c-n-k-c-n-1-k-c-n-1-k-1
#     :param self:
#     :param NN:
#     :param K:
#     :return:
#     """
#     result = [[[]]]
#     for n in range(1, NN + 1):
#         newRes = [[[]]]  # C(n, 0) = 0
#         for k in range(1, n):
#             # C(n, k) = C(n-1, k) + C(n-1, k-1)
#             newRes.append(result[k] + [_ + [n] for _ in result[k - 1]])
#             # C(n, n) = C(n-1, n-1) = 1
#         newRes.append([result[n - 1][0] + [n]])
#         result = newRes
#     return result[K]


if __name__ == '__main__':
    # test only
    print([i for i in mask_same_digits(222323, 3)])
    print([i for i in mask_same_digits(323333, 3)])
    print('-' * 30)

    caches = {}
    for i in prime_sieve(1000000):
        for seq in mask_same_digits(i, 3):
            caches.setdefault(seq, []).append(i)
    print('> caches %d' % len(caches))

    for k in caches:
        if len(caches[k]) >= 8:
            print((k, len(caches[k])), caches[k])  # 121313
