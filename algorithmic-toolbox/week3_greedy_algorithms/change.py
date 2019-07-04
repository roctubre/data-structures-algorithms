# Uses python3
import sys

def get_change(m):
    tens = m // 10
    m = m % 10
    fives = m // 5
    m = m % 5
    
    return tens + fives + m

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
