# Uses python3
import sys
import random

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
    
    
def get_fibonacci_last_digit(n):
    a = 0
    b = 1
    
    for i in range(n):
        x = (a + b) % 10
        a = b
        b = x
    
    return a
    
def stresstest(n):
    random.seed(1)
    for _ in range(n):
        r = random.randint(0,10000)
        if get_fibonacci_last_digit_naive(r) != get_fibonacci_last_digit(r):
            print("Error!", r)
            return
    
    print("All OK.")
    

if __name__ == '__main__':
    #stresstest(1000)
    input = sys.stdin.readline()
    n = int(input)
    print(get_fibonacci_last_digit(n))
