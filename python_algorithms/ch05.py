def checkerboard_covering():
    pass

def walk(G, s):
    P, Q = dict(), set(G)
    P[s] = None  # no predecessor
    while Q:
        u = Q.pop()
        for v in G[u].difference(P):
            # Q.add(v)
            P[v] = u
    return P

def component(G):
    seen, comp = set(), []
    for u in G:
        if u not in seen:
            C = walk(G, u)
            seen.update(C)
            comp.append(C)
    return comp

def dfs_topsort(G):
    res, S = [], set()
    def recurse(u):
        if u in S: return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    # res.reverse()
    return res

if __name__ == '__main__':
    G = {
        'a': set('bcdef'),
        'b': set('ce'),
        'c': set('d'),
        'd': set('e'),
        'e': set('f'),
        'f': set('cgh'),
        'g': set('fh'),
        'h': set('fg'),
    }
    print(walk(G, 'b'))
    print(component(G))
    print(dfs_topsort(G))

