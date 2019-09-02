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
    order = sort_characters(text)
    classes = compute_char_classes(text, order)
    shiftlen = 1
    while shiftlen < len(text):
        order = sort_doubled(text, shiftlen, order, classes)
        classes = update_classes(order, classes, shiftlen)
        shiftlen *= 2

    return order

def bwt_from_suffixarray(text, suffixarray):
    # create count array
    starts = dict()
    counter = dict()
    occ_count_before = [dict() for _ in range(len(suffixarray)+1)]

    for i, c in enumerate(suffixarray):
        nextchar = c - 1
        for k, v in counter.items():
            occ_count_before[i][k] = v
        if not text[nextchar] in counter:
            counter[text[nextchar]] = 0
        counter[text[nextchar]] += 1

    # add last row to count array
    for k, v in counter.items():
        occ_count_before[len(suffixarray)][k] = v
    
    # create dictionary with starting indices
    templist = sorted([(k,v) for k,v in counter.items()], key=lambda x: x[0])
    summing = 0
    for item in templist:
        starts[item[0]] = summing
        summing += item[1]
        
    return starts, occ_count_before

def pattern_matching(pattern, starts, occ_counts_before):
    top = 0
    bottom = len(occ_counts_before) - 2
    idx = 1

    while top <= bottom:
        if idx <= len(pattern):
            symbol = pattern[-idx]

            count_top = 0
            count_bottom = 0
            if symbol in occ_counts_before[top]:
                count_top = occ_counts_before[top][symbol]
            if symbol in occ_counts_before[bottom+1]:
                count_bottom = occ_counts_before[bottom+1][symbol]

            if count_bottom - count_top > 0:
                top = starts[symbol] + count_top
                bottom = starts[symbol] + occ_counts_before[bottom+1][symbol] - 1
            else:
                return None
        else:
            break
        idx += 1
    
    return (top, bottom)

def find_occurrences(text, patterns):
    occs = set()
    text = ''.join([text, "$"])
    suffix_array = build_suffix_array(text)
    starts, occ_count_before = bwt_from_suffixarray(text, suffix_array)
    
    for p in patterns:
        result = pattern_matching(p, starts, occ_count_before)
        if result:
            occs = occs | set(suffix_array[result[0]:result[1]+1])

    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))