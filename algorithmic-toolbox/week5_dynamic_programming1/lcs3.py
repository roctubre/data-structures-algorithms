#Uses python3

import sys
import numpy as np

def lcs3(a, b, c):
    d = np.zeros((len(a)+1, len(b)+1, len(c)+1)).astype(int)
    
    for k in range(1, len(c)+1):
        for j in range(1, len(b)+1):
            for i in range(1, len(a)+1):
                scores = [d[i, j, k-1],
                          d[i, j-1, k],
                          #d[i, j-1, k-1],
                          d[i-1, j, k]
                          #d[i-1, j, k-1],
                          #d[i-1, j-1, k]
                          ]
                
                
                if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                    scores.append(d[i-1, j-1, k-1] + 1)
                    d[i, j, k] = max(scores)
                else:
                    scores.append(d[i-1, j-1, k-1])
                    d[i, j, k] = max(scores)
        
    
    return d[len(a), len(b), len(c)]

    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
    