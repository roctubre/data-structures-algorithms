# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum(from_, to):
    period = get_period(10)
    remainder_from = from_ % period
    remainder_to = to % period
    
    if remainder_from > remainder_to:
        remainder_to += period

    sum = 0
    for i in range(remainder_from, remainder_to + 1):
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
    input = sys.stdin.readline();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))