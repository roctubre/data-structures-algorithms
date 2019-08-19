#!/usr/bin/python3

import sys
import queue
import math

class PQNode:
    def __init__(self, k):
        self.key = k
        self.done = False

    def __lt__(self, other):
        return self.key < other.key


class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion 
        self.inf = float("inf")       
        self.n = n
        self.adj = adj
        self.cost = cost
        self.d = [self.inf]*n
        self.dm = [self.inf]*n
        self.visited = [False]*n
        self.workset = set()
        # Coordinates of the nodes
        self.x = x
        self.y = y

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            self.visited[v] = False
            self.dm[v] = self.inf
            #self.cost2[v] = [None for _ in range(len(self.cost[v]))]

        self.workset = set()

    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, qdict, v, dist, measure):
        if self.dm[v] > measure:
            self.visited[v] = True
            self.workset.add(v)
            self.d[v] = dist
            self.dm[v] = measure

            # change priority
            if v in qdict:
                qdict[v].done = True
            node = PQNode(v)
            q.put_nowait((measure, node))
            
            qdict[v] = node

    def pfunc(self, u, v):
        return ((self.x[u]-self.x[v])**2+(self.y[u]-self.y[v])**2)**0.5

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        if s == t:
            return 0
        self.clear()
        q = queue.PriorityQueue()
        qdict = dict()
        
        self.visit(q, qdict, s, 0, 0)
        while q.qsize() != 0:
            u = q.get_nowait()
            u = u[1]
            if t == u.key or u.done:
                continue
            if self.visited[t] and self.dm[u.key] > self.dm[t]:
                break

            for vi, v in enumerate(self.adj[u.key]):
                vcost = self.cost[u.key][vi]
                dt = vcost - self.pfunc(v, t)
                self.visit(q, qdict, v, self.d[u.key]+vcost, self.d[u.key]+dt)

        return self.d[t] if self.d[t] != self.inf else -1


def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))
