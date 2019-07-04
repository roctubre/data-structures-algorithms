#Uses python3

import sys
import math

def largest_number(a):
    res = ""
    
    l = a.copy()
    
    while len(l) != 0:
        maxDigit = -math.inf
        for digit in l:
            if isGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        res += str(maxDigit)
        l.remove(maxDigit)
    
    return res
    
    
def isGreaterOrEqual(a, b):
    if b == -math.inf:
        return True

    str_a = str(a)
    str_b = str(b)
    
    adjusted = True

    while adjusted:
        adjusted = False
        min_len = min(len(str_a), len(str_b))
        if len(str_a) < len(str_b):
            while str_b[:min_len] == str_a:
                str_b = str_b[min_len:]
                adjusted = True
        elif len(str_a) > len(str_b):
            while str_a[:min_len] == str_b:
                str_a = str_a[min_len:]
                adjusted = True
        
        if str_b == "" or str_a == "":
            return True
    
    min_len = min(len(str_a), len(str_b))

    a_cut = int(str_a[:min_len])
    b_cut = int(str_b[:min_len])
    
    if a_cut > b_cut:
        return True

    return False

    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
