#Uses python3
import sys
import math

def mergesort(a, axis=0):
    if not a:
        return []
    if len(a) == 1:
        return a
    m = len(a) // 2

    b = mergesort(a[0:m], axis)
    c = mergesort(a[m:len(a)], axis)

    a = merge(b, c, axis)

    return a
    
def merge(a, b, axis=0):
    r = []

    while a and b:
        if a[0][axis] < b[0][axis]:
            r.append(a.pop(0))
        else:
            r.append(b.pop(0))

    # append remaining elements to result array
    if a:
        r = r + a
    if b:
        r = r + b
        
    return r

def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5

    
def minimum_distance(x, y):
    #write your code here
    a = list(zip(x, y))
    a = mergesort(a, axis=0)
    d = min_recursive(a)

    return d

def min_recursive(s):
    if len(s) == 2:
        return distance(s[0], s[1])
    elif len(s) == 3:
        d1 = distance(s[0], s[1])
        d2 = distance(s[0], s[2])
        d3 = distance(s[1], s[2])
        return min(d1, d2, d3)
    
    mid = len(s) // 2

    s1 = s[:mid]
    s2 = s[mid:]

    d1 = min_recursive(s1)
    d2 = min_recursive(s2)
    d = min(d1, d2)
    
    s = [p for p in s if abs(s[mid][0]-p[0]) < d]
    
    s = mergesort(s, axis=1)
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if abs(s[i][1] - s[j][1]) > d:
                break
            d = min(d, distance(s[i], s[j]))

    
    return d
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    
