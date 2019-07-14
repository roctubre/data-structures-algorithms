# Uses python3
import sys
import itertools
import numpy as np

def partition3(A):
    total = sum(A)
    if total % 3 != 0:
        return 0
    
    sequences1 = partition2(A, total//3)
    if sequences1:
        for seq in sequences1:
            B = A.copy()
            for e in seq:
                B.remove(e)
            
            sequences2 = partition2(B, total//3)
            if sequences2:
                return 1
    
    return 0

    
def partition2(A, target):
    values = np.zeros((len(A)+1, target+1)).astype(int)
    for n in range(1, len(A)+1):
        for i in range(1,target+1):
            values[n,i] = values[n-1,i]
            if A[n-1] <= i:
                val = A[n-1]
                if values[n-1, i-A[n-1]]:
                    val += (i-A[n-1])
                values[n,i] = values[n,i] or (val == i)

    
    sequences = []
    for a in range(len(A), 0, -1):
        seq = []
        backward = target
        if values[a, target]:
            for i in range(a, 0,-1):
                if backward == 0:
                    break
                if backward - A[i-1] >= 0:
                    backward -= A[i-1]
                    seq.append(A[i-1])
        else:
            break
            
        sequences.append(seq)
        
    return sequences

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

