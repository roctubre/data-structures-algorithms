# Uses python3
import sys
import random


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
    
def lcm(a, b):
    return (a*b) // gcd(a,b)

    
def gcd(a, b):
    x = a % b
    if x >= 1:
        return gcd(b, x)
        
    return b
    
    
if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))
    
