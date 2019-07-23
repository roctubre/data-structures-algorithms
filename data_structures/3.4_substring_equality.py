# python3

import sys


_multiplier = 263
_prime1 = 1000000007
_prime2 = 1000000009

class Solver:
    def __init__(self, s):
        self.s = s
        self.h1 = [0]
        self.h2 = [0]
        self.factors1 = [1]
        self.factors2 = [1]
        
        for i in range(0, len(s)):
            self.h1.append((self.h1[-1]*_multiplier + ord(s[i])) % _prime1)
            self.h2.append((self.h2[-1]*_multiplier + ord(s[i])) % _prime2)
            
            self.factors1.append((self.factors1[-1]*_multiplier) % _prime1)
            self.factors2.append((self.factors2[-1]*_multiplier) % _prime2) 
        
    def ask(self, a, b, l):
        h1_a = (self.h1[a+l] - self.factors1[l]*self.h1[a]) % _prime1
        h1_b = (self.h1[b+l] - self.factors1[l]*self.h1[b]) % _prime1
        h2_a = (self.h2[a+l] - self.factors2[l]*self.h2[a]) % _prime2
        h2_b = (self.h2[b+l] - self.factors2[l]*self.h2[b]) % _prime2
        return (h1_a == h1_b and h2_a == h2_b)

        
if __name__ == "__main__":
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")
