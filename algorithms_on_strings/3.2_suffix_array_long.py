# python3
import sys


def sort_characters(text):
    order = [0] * len(text)
    count = dict()
    for c in text:
        if not c in count:
            count[c] = 0
        count[c] += 1

    countlist = sorted([(c,v) for c,v in count.items()], key=lambda x: x[0])
    summed = 0
    for i in range(0, len(countlist)):
        c, v = countlist[i]
        summed += v
        count[c] = summed
    
    for i in range(len(text)-1, -1, -1):
        c = text[i]
        count[c] -= 1
        order[count[c]] = i

    return order

def compute_char_classes(text, order):
    classes = [0] * len(text)
    for i in range(1, len(text)):
        if text[order[i]] != text[order[i-1]]:
            classes[order[i]] = classes[order[i-1]] + 1
        else:
            classes[order[i]] = classes[order[i-1]]
    return classes

def sort_doubled(text, shiftlen, order, classes):
    count = [0] * len(text)
    newOrder = [0] * len(text)
    for i in range(len(text)):
        count[classes[i]] += 1
    for j in range(1, len(text)):
        count[j] += count[j-1]
    for i in range(1, len(text)+1):
        start = (order[-i] - shiftlen + len(text)) % len(text)
        cl = classes[start]
        count[cl] -= 1
        newOrder[count[cl]] = start
    return newOrder

def update_classes(newOrder, classes, shiftlen):
    n = len(newOrder)
    newClasses = [0] * n
    for i in range(1, n):
        cur = newOrder[i]
        prev = newOrder[i-1]
        mid = (cur + shiftlen) % n
        midPrev = (prev + shiftlen) % n
        if classes[cur] != classes[prev] or classes[mid] != classes[midPrev]:
            newClasses[cur] = newClasses[prev] + 1
        else:
            newClasses[cur] = newClasses[prev]
    return newClasses

def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = sort_characters(text)
    classes = compute_char_classes(text, order)
    shiftlen = 1
    while shiftlen < len(text):
        order = sort_doubled(text, shiftlen, order, classes)
        classes = update_classes(order, classes, shiftlen)
        shiftlen *= 2

    return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
