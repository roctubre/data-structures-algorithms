# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

    
def get_fibonacci_huge(n, m):
    period = get_period(m)
    remainder = n % period
    return calc_fib(remainder) % m
    
    
def calc_fib(n):
    a = 0
    b = 1
        
    for i in range(n):
        x = a + b
        a = b
        b = x
       
    return a

    
def get_period(m):
    i = 2
    while True:
        if calc_fib(i)%m == 0 and calc_fib(i+1)%m == 1:
            return i
        i += 1

    
if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
    