# Uses python3
import sys
import random

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

    
def fibonacci_sum(n):

    period = get_period(10)
    remainder = n % period
    sum = 0
    for i in range(remainder + 1):
        sum = (sum + calc_fib(i)) % 10
    
    return sum

    
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
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum(n))
