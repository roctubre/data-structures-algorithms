#Uses python3

import sys

def shortest_paths(adj, cost, s, dist, reach, shortest):
    n = len(adj)
    prev = [None for _ in range(n)]
    dist[s] = 0
    reach[s] = 1
    last_changes = []
    changes = False
    
    for i in range(n):
        changes = False
        for u in range(n):
            for vi, v in enumerate(adj[u]):
                if dist[v] > dist[u] + cost[u][vi]:
                    if not reach[v]:
                        reach[v] = 1
                    dist[v] = dist[u] + cost[u][vi]
                    prev[v] = u
                    changes = True
                    if i+1 == n:
                        last_changes.append(v)
        if not changes:
            break
    
    # get negative cycles and set none shortest distance
    for u in last_changes:
        x = u
        if not shortest[u]:
            continue
        for _ in range(n):
            shortest[x] = 0
            x = prev[x]
    
    # set none shortest distance when reachable from a negative cycle
    for u in range(n*n):
        u = u % n
        if not shortest[u]:
            for v in adj[u]:
                shortest[v] = 0


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

