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

def minimum_distance(x, y):
    result = 0.
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
            result += d[0]
            union(parent, rank, d[1][0], d[1][1])

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
