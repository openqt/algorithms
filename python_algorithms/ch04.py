def checkerboard_covering():
    pass

def radixsort(seq):
    pass

def insertion_sort(seq):
    for i in range(1, len(seq)):
        # for j in range(i+1):
        #     if seq[j] >= seq[i]:
        #         break
        # v = seq[i]
        # for k in range(i, j, -1):
        #     seq[k] = seq[k-1]
        # seq[j] = v
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def insertion_sort_rec(seq, i=0):
    if i >= len(seq): return seq

    # for j in range(i+1):
    #     if seq[j] >= seq[i]:
    #         break
    # v = seq[i]
    # for k in range(i, j, -1):
    #     seq[k] = seq[k-1]
    # seq[j] = v
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    return insertion_sort_rec(seq, i+1)

def selection_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        l = i
        for j in range(i+1):
            if seq[j] > seq[l]:
                l = j
        seq[l], seq[i] = seq[i], seq[l]
    return seq

def next_permutation(a):
    """Generate the lexicographically next permutation inplace.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    Return false if there is no next permutation.
    """
    # Find the largest index i such that a[i] < a[i + 1]. If no such
    # index exists, the permutation is the last permutation
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break  # found
    else:  # no break: not found
        return None  # no next permutation

    # Find the largest index j greater than i such that a[i] < a[j]
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    # Swap the value of a[i] with that of a[j]
    a[i], a[j] = a[j], a[i]

    # Reverse sequence from a[i + 1] up to and including the final element a[n]
    a[i + 1:] = reversed(a[i + 1:])
    return a

from collections import Counter
def max_permutation(seq):
    C = Counter(seq)
    Q = [i for i in range(len(seq)) if C[i] == 0]
    A = set(range(len(seq)))
    while Q:
        i = Q.pop()
        A.remove(i)
        C[seq[i]] -= 1
        if C[seq[i]] == 0:
            Q.append(seq[i])
    return A

from collections import defaultdict
def counting_sort(seq):
    val, C = [], defaultdict(list)
    for i in seq: C[i].append(i)
    for i in range(min(C), max(C)+1):
        val.extend(C[i])
    return val

if __name__ == '__main__':
    from random import randrange
    seq = [randrange(100) for i in range(20)]
    print(seq)
    print(selection_sort(seq.copy()))
    print(insertion_sort(seq.copy()))
    print(insertion_sort_rec(seq.copy()))

    print(next_permutation(list("137652")))
    print(max_permutation([int(i) for i in "22053574"]))

    print(counting_sort(seq.copy()))
