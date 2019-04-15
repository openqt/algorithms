# lc218 hte skyline
def huffman(seq, frq):
    pass


def codes(tree, prefix=""):
    pass

def kruskal(G):
    pass

import heapq
def prim(G, s):
    P, Q = {}, [(0, None, s)]
    while Q:
        _, p, u = heapq.heappop(Q)
        if u in P: continue
        P[u] = p
        for v, w in G[u].items():
            heapq.heappush(Q, (w, u, v))
    return P


if __name__ == '__main__':
    print(huffman("abcdefghi", [4, 5, 6, 9, 11, 12, 15, 16, 20]))
