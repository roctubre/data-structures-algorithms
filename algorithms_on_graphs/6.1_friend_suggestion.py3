#!/usr/bin/python3

import sys
import heapq

class QNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.done = False
    
    def __lt__(self, other):
        return self.key < other.key

class BiDij:
    def __init__(self, n):
        self.n = n                              # Number of nodes
        self.inf = float("inf")                 # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [[False]*n, [False]*n]   # visited[v] == True iff v was visited by forward or backward search
        self.workset = set()                       # All the nodes visited by forward or backward search

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[0][v] = False
            self.visited[1][v] = False

        self.workset = set()

    def visit(self, q, side, v, dist, qdict):
        """Try to relax the distance to node v from direction side by value dist."""
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            self.visited[side][v] = True
            self.workset.add(v)

            # change priority
            if v in qdict[side]:
                qdict[side][v].done = True

            node = QNode(self.d[side][v], v)
            qdict[side][v] = node
            heapq.heappush(q[side], node)
        
        pass
    
    def shortestPath(self, s, t):
        distance = self.inf
        for u in self.workset:
            if self.d[0][u] + self.d[1][u] < distance:
                distance = self.d[0][u] + self.d[1][u]
        
        return distance

    def query(self, adj, cost, s, t):
        self.clear()
        q = [[], []]
        qdict = [dict(), dict()]
        self.visit(q, 0, s, 0, qdict)
        self.visit(q, 1, t, 0, qdict)

        while q[0] and q[1]:
            if q[0]:
                u = heapq.heappop(q[0])
                if not u.done:
                    for vi in range(len(adj[0][u.value])):
                        v = adj[0][u.value][vi]
                        vcost = cost[0][u.value][vi]
                        self.visit(q, 0, v, u.key+vcost, qdict)
                    if self.visited[1][u.value]:
                        return self.shortestPath(s, t)
            if q[1]:
                u = heapq.heappop(q[1])
                if not u.done:
                    for vi in range(len(adj[1][u.value])):
                        v = adj[1][u.value][vi]
                        vcost = cost[1][u.value][vi]
                        self.visit(q, 1, v, u.key+vcost, qdict)

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
