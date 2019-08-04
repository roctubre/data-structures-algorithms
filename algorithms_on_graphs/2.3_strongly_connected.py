#Uses python3

import sys


def reverseGraph(adj):
    n = len(adj)
    r_adj = [[] for _ in range(n)]
    for idx in range(n):
        for w in adj[idx]:
            r_adj[w].append(idx)
    return r_adj


def number_of_strongly_connected_components(adj):
    result = 0
    n = len(adj)
    r_adj = reverseGraph(adj)
    
    # DFS on reverse G
    visited = [False] * n
    current = None
    order = []
    for v in range(n):
        stack = []
        running_visit = [False] * n
        if visited[v]:
            continue
        elif not r_adj[v]:
            visited[v] = True
            order.append(v)
            continue

        current = [v, r_adj[v].copy()]
        
        while current:
            running_visit[current[0]] = True
            next = False
            for idx in range(len(current[1])-1, -1, -1):
                w = current[1][idx]
                if not running_visit[w]:
                    current[1].pop()
                    stack.append(current)
                    current = [w, r_adj[w]]
                    next = True
                    break
            if next:
                continue
            else:
                if not visited[current[0]]:
                    order.append(current[0])
                    visited[current[0]] = True
                running_visit[current[0]] = False
                current = stack.pop() if stack else None
    
    # SCC
    visited = [False] * n
    current = None

    for v in reversed(order):
        stack = []
        if visited[v]:
            continue
        elif not adj[v]:
            visited[v] = True
            result += 1
            continue

        result += 1
        current = v
        while current != None:
            visited[current] = True
            next = False
            for w in adj[current]:
                if not visited[w]:
                    stack.append(current)
                    current = w
                    next = True
                    break
            if next:
                continue
            else:
                current = stack.pop() if stack else None

    return result
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
