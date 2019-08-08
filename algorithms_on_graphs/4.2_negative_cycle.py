#Uses python3

import sys


def negative_cycle(adj, cost):
    n = len(adj)
    dist = [float("inf") for _ in range(n)]
    prev = [None for _ in range(n)]
    last_change = 0
    changes = False

    for _ in range(n):
        changes = False
        for u in range(n):
            if dist[u] == float("inf"):
                dist[u] = 0
            for vi, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][vi]:
                    dist[v] = dist[u] + cost[u][vi]
                    prev[v] = u
                    last_change = v
                    changes = True
        if not changes:
            break
    
    if changes:
        x = last_change
        for _ in range(n):
            x = prev[x]
        
        y = x
        p = [y]
        while True:
            x = prev[x]
            p.append(x)
            if x == y:
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
