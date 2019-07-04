# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # get value per unit
    v_u = [(v, w, v/w) for w, v in zip(weights, values)]
    v_u = sorted(v_u, key=lambda x: x[2], reverse = True)

    for idx in range(len(v_u)):
        if capacity == 0:
            return value
        
        a = min(v_u[idx][1], capacity)
        value = value + a*v_u[idx][2]
        capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
