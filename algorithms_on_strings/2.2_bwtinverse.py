# python3
import sys


def InverseBWT(bwt):
    counter = dict()

    # process first and last column in one loop
    blist = []
    orderedlist = []
    for c in bwt:
        if not c in counter:
            counter[c] = 0
        blist.append((c, counter[c]))
        counter[c] += 1

    # order counter items into a list
    orderedlist = sorted([(k,v) for k,v in counter.items()], 
                         key=lambda x: x[0])
    
    # create dictionary with running indexes
    counter.clear()
    summed = 0
    for element in orderedlist:
        counter[element[0]] = summed
        summed += element[1]

    # reconstruct string
    result = [""] * len(bwt)
    result[-1] = "$"
    current = blist[0]
    for i in range(2, len(bwt)+1):
        result[-i] = current[0]
        cindex = counter[current[0]] + current[1]
        current = blist[cindex]

    return ''.join(result)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))