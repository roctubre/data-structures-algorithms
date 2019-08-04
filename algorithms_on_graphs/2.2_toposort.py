#Uses python3

import sys

def toposort(adj):
    n = len(adj)
    order = []
    visited = [False] * n
    current = None
    
    for v in range(n):
        stack = []
        if visited[v]:
            continue
        elif not adj[v]:
            visited[v] = True
            order.append(v)
            continue

        current = [v, adj[v].copy()]
        while current:
            next = False
            for idx in range(len(current[1])-1, -1, -1):
                w = current[1][idx]
                if not visited[w]:
                    current[1].pop()
                    stack.append(current)
                    current = [w, adj[w]]
                    next = True
                    break
            if next:
                continue
            else:
                if not visited[current[0]]:
                    order.append(current[0])
                    visited[current[0]] = True
                current = stack.pop() if stack else None

    return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

