#!/usr/bin/python3

import sys
import heapq
from math import sqrt

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # constant variables
        self.inf = float("inf")       
        self.n = n
        self.adj = adj
        self.cost = cost
        self.x = x
        self.y = y

        # query variables
        self.d = [self.inf]*n
        self.processed = [False]*n


    def clear(self):
        """ Reset calculated distances and visited status for next query """
        self.d = [self.inf] * self.n
        self.processed = [False] * self.n


    def potential(self, u, v):
        """ Using Euclidean distance as potential function """
        return sqrt((self.x[u]-self.x[v])**2+(self.y[u]-self.y[v])**2)

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        """ Calculate shortest distance between start and target node """

        # check if start and target node are the same
        if s == t:
            return 0

        # clear artefacts from previous query
        self.clear()

        # set up priority queue and add starting node as first element
        q = []
        self.d[s] = 0
        heapq.heappush(q, (self.potential(s, t), s))

        # search and discover
        while q:
            u = heapq.heappop(q)[1]

            # continue if current node was already processed
            if self.processed[u]:
                continue

            # exit condition is when current node equals target node
            if t == u:
                break

            # loop through connected nodes
            for vi, v in enumerate(self.adj[u]):
                if self.processed[v]:
                    continue

                # accumulated real distance since starting node to this (v) node
                v_g = self.d[u] + self.cost[u][vi]

                # add to queue if new calculated distance is smaller
                if self.d[v] > v_g:
                    self.d[v] = v_g
                    heapq.heappush(q, (v_g + self.potential(v, t), v))

            # set current node as processed
            self.processed[u] = True

        # return distance of target node
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
