#Uses python3

import sys
from queue import Queue

def distance(adj, s, t):
    queue = Queue()
    distance = [-1] * len(adj)
    queue.put(s)
    distance[s] = 0
    while not queue.empty():
        u = queue.get_nowait()
        for v in adj[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                if v == t:
                    return distance[v]
                queue.put(v)
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
