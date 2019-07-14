# Uses python3
import sys
import numpy as np

def optimal_weight(W_max, weights):
    value = np.zeros((len(weights)+1, W_max+1))
    for item in range(1, len(weights)+1):
        for w in range(1, W_max+1):
            value[item, w] = value[item-1, w]
            if weights[item-1] <= w:
                val = value[item-1, w-weights[item-1]] + weights[item-1]
                if val > value[item, w]:
                    value[item, w] = val

    return int(value[len(weights), W_max])


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
