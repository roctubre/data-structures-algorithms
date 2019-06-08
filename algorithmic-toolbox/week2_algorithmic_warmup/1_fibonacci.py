# Uses python3
import time


def calc_fib_old(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
    

def calc_fib_list(n):
    arr = list()
    arr.append(0)
    arr.append(1)
    
    if n <= 1:
        return arr[n]
    
    for i in range(2, n + 1):
        arr.append(arr[i-2] + arr[i-1])

    return arr[n]
    

def calc_fib(n):
    a = 0
    b = 1
        
    for i in range(n):
        x = a + b
        a = b
        b = x
       
    return a

if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
    
    """
    start = time.time()
    calc_fib_old(n)
    print("Old - Time: {:.6f} seconds".format(time.time() - start))
    start = time.time()
    calc_fib_list(n)
    print("List - Time: {:.6f} seconds".format(time.time() - start))
    start = time.time()
    calc_fib(n)
    print("Var - Time: {:.6f} seconds".format(time.time() - start))
    """