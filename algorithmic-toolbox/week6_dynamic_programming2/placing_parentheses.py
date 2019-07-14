# Uses python3
import numpy as np
import math


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    digits = dataset[::2]
    ops = dataset[1::2]
    n = len(digits)
    
    m = np.zeros((len(digits), len(digits)))
    M = np.zeros((len(digits), len(digits)))
    
    for i in range(len(digits)):
        m[i,i] = digits[i]
        M[i,i] = digits[i]
    
    for s in range(1, n):
        for i in range(n-s):
            j = i + s
            m[i,j], M[i,j] = minNmax(m,M,ops,i,j)
    
    return int(M[0,n-1])

def minNmax(m, M, ops, i, j):
    minimum = math.inf
    maximum = -math.inf
    
    for k in range(i, j):
        a = evalt(M[i,k], M[k+1,j], ops[k])
        b = evalt(M[i,k], m[k+1,j], ops[k])
        c = evalt(m[i,k], M[k+1,j], ops[k])
        d = evalt(m[i,k], m[k+1,j], ops[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
        
    return minimum, maximum


if __name__ == "__main__":
    print(get_maximum_value(input()))
