# python3


def max_sliding_window(sequence, m):
    window = []
    maximums = []
    for i in range(len(sequence)):
        if window and window[0] < sequence[i]:
            window.clear()
        while window and window[-1] < sequence[i]:
            window.pop()
        
        window.append(sequence[i])
        
        if i < m:
            if i == m-1:
                maximums.append(max(window))
            continue
        
        popidx = i - m
        if len(window) > 1 and sequence[popidx] == window[0]:
            window.pop(0)
        
        maximums.append(window[0])
        
    return maximums

    
if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding_window(input_sequence, window_size))))

