#Uses python3
import sys
import heapq


def find(parents, ranks, i):
    if i != parents[i]:
        parents[i] = find(parents, ranks, parents[i])
    return parents[i]

def union(parents, ranks, i, j):
    i_id = find(parents, ranks, i)
    j_id = find(parents, ranks, j)
    if i_id == j_id:
        return
    if ranks[i_id] > ranks[j_id]:
        parents[j_id] = i_id
    else:
        parents[i_id] = j_id
        if ranks[i_id] == ranks[j_id]:
            ranks[j_id] += 1

def clustering(x, y, k):
    edges = []
    n = len(x)

    parent = [i for i in range(n)]
    rank = [0] * n

    # create heap with all distances
    dist = []
    for u in range(n):
        for v in range(n):
            if u != v:
                d = ((x[u]-x[v])**2+(y[u]-y[v])**2)**0.5
                heapq.heappush(dist, (d, (u, v)))
    
    # Kruskal's algorithm
    while dist:
        d = heapq.heappop(dist)
        if find(parent, rank, d[1][0]) != find(parent, rank, d[1][1]):
            edges.append(d)
            union(parent, rank, d[1][0], d[1][1])

    return edges[-(k-1)][0]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
