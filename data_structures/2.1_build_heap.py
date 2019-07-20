# python3


def parent(i):
    return (i - 1) // 2
    
    
def leftChild(i):
    return i*2 + 1

    
def rightChild(i):
    return i*2 + 2 

    
def siftDown(data, i):
    minIndex = i
    l = leftChild(i)
    r = rightChild(i)
    swaps = []
    
    if l < len(data) and data[l] < data[minIndex]:
            minIndex = l
            
    if r < len(data) and data[r] < data[minIndex]:
            minIndex = r 
    
    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        swaps.append((i, minIndex))
        swaps += siftDown(data, minIndex)
    
    return swaps
    
    
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps = []
    for i in range(len(data)//2, -1, -1):
        swaps += siftDown(data, i)
    
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
