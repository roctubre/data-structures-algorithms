# Uses python3
import numpy as np


def edit_distance(s, t):
    d = np.zeros((len(s)+1, len(t)+1))

    for j in range(0, len(t)+1):
        for i in range(0, len(s)+1):
            if i == 0:
                d[i, j] = j
                continue
            elif j == 0:
                d[i, j] = i
                continue
                
            insertion = d[i, j-1] + 1
            deletion = d[i-1, j] + 1
            match = d[i-1, j-1]
            mismatch = d[i-1, j-1] + 1
            
            if s[i-1] == t[j-1]:
                d[i, j] = min(insertion, deletion, match)
            else:
                d[i, j] = min(insertion, deletion, mismatch)
    
    return int(d[len(s), len(t)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
