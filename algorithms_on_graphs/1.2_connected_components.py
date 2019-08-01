#Uses python3

import sys


def number_of_components(adj):
    counter = 1
    visited = [0 for _ in range(len(adj))]
    stack = []
    for i in range(len(adj)):
        if visited[i]:
            continue
        curr = i
        while curr != None:
            visited[curr] = counter
            explore = False
            for next in adj[curr]:
                if not visited[next]:
                    stack.append(curr)
                    curr = next
                    explore = True
                    break
            if not explore:
                if stack:
                    curr = stack.pop()
                else:
                    curr = None
        counter += 1
    
    return counter - 1

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
    print(number_of_components(adj))
