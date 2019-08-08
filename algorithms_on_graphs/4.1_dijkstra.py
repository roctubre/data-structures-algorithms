#Uses python3

import queue
import sys
import heapq

class QNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, other):
        return self.key < other.key

        
def distance(adj, cost, s, t):
    n = len(adj)
    dist = []
    prev = []
    h = []
    for u in range(n):
        if u == s:
            dist.append(0)
        else:
            dist.append(10**4)
        prev.append(None)
        heapq.heappush(h, QNode(dist[-1], u))

    while h:
        # extract min
        u = heapq.heappop(h)
        for vi in range(len(adj[u.value])):
            v = adj[u.value][vi]
            vcost = cost[u.value][vi]
            if dist[v] > u.key + vcost:
                dist[v] = u.key + vcost
                prev[v] = u.value
                # change priority
                idx = [i for i,x in enumerate(h) if v == x.value]
                
                if idx:
                    idx = idx[0]
                    oldp = h[idx].key
                    h[idx].key = dist[v]
                    if dist[v] < oldp:
                        heapq._siftdown(h, 0, idx)
                    else:
                        heapq._siftup(h, idx)
                else:
                    heapq.heappush(h, QNode(dist[v], v))

    return dist[t] if dist[t] <= 10**3 else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
