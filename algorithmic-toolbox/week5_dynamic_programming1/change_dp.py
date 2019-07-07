# Uses python3
import sys
import math

def get_change(m, coins=[1, 3, 4]):
    minNumCoins = [0]
    
    for m in range(1, m+1):
        minNumCoins.append(math.inf)
        for coin in coins:
            if m >= coin:
                numCoins = minNumCoins[m-coin] + 1
                if numCoins < minNumCoins[m]:
                    minNumCoins[m] = numCoins
    
    return minNumCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
