# Uses python3
import sys
import math


def optimal_sequence_greedy(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return list(reversed(sequence))
    
def optimal_sequence(n):
    nums = [0, 0]
    sequence = [n]
    for i in range(2, n+1):
        #nums.append(math.inf)
        cnt = math.inf
        if i % 3 == 0:
            cnt = nums[i//3]
        if i % 2 == 0:
            cnt = min(cnt, nums[i//2])
        
        cnt = min(cnt, nums[i-1])
        nums.append(cnt+1)
    
    
    while n != 1:
        idx = n - 1
        
        if n % 3 == 0 and nums[n//3] < nums[idx]:
            idx = n // 3
            
        if n % 2 == 0 and nums[n//2] < nums[idx]:
            idx = n // 2
        
        n = idx
        sequence.append(idx)
            
    return list(reversed(sequence))  
    
if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)

    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

    