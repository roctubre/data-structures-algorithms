#Uses python3

import sys
from queue import Queue

def bipartite(adj):
    n = len(adj)
    color = [-1] * n

    for u in range(n):
        if color[u] == -1:
            queue = Queue()
            queue.put(u)
            color[u] = 0
            while not queue.empty():
                u = queue.get_nowait()
                #print(u, color)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 if color[u] == 0 else 0
                        queue.put(v)
                    elif color[v] == color[u]:
                        return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
