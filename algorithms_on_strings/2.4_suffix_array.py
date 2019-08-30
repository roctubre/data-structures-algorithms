# python3
import sys
import heapq

def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    # using a heapqueue to add and sort them at the same time 
    h = []
    for i in range(len(text)):
        heapq.heappush(h, (text[i:], i))

    # create result list by comprehension; suffixes are popped off the heap in order
    return [heapq.heappop(h)[1] for _ in range(len(text))]


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
