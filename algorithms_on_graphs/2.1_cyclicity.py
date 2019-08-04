#Uses python3

import sys


def acyclic(adj):
    n = len(adj)
    visited2 = [False] * n
    visit_running = [False] * n
    current = None
    
    for v in range(n):
        stack = []
        if not adj[v] or visited2[v]:
            visited2[v] = True
            continue
        stack.append([v, adj[v].copy()])
        visit_running = [False] * n
        visit_running[v] = True
        u = stack[-1][1].pop()
        current = [u, adj[u].copy()]

        while current:
            visited2[current[0]] = True
            visit_running[current[0]] = True
            next = False
            for idx in range(len(current[1])-1, -1, -1):
                w = current[1][idx]
                if not visit_running[w]:
                    current[1].pop()
                    stack.append(current)
                    current = [w, adj[w]]
                    next = True
                    break
                else:
                    return 1
            if next:
                continue
            elif not stack:
                current = None
            else:
                visit_running[current[0]] = False
                current = stack.pop()

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
