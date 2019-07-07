#Uses python3

import sys
import numpy as np

    
def lcs2(s, t):
    d = np.zeros((len(s)+1, len(t)+1)).astype(int)
    
    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):
            insertion = d[i, j-1]
            deletion = d[i-1, j]
            match = d[i-1, j-1] + 1
            mismatch = d[i-1, j-1]
            
            if s[i-1] == t[j-1]:
                d[i, j] = max(insertion, deletion, match)
            else:
                d[i, j] = max(insertion, deletion, mismatch)            
        
    
    return d[len(s), len(t)]

    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
