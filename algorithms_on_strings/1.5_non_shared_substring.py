# python3
import sys
import heapq

def solve(p, q):
    """
    Build a suffix tree of the joined strings and return the shortest
	(non-empty) substring of p that does not appear in q
    """

    class Node():
        def __init__(self, parent, rank, mode, offsets):
            self.parent = parent
            self.rank = rank
            self.mode = mode
            self.children = dict()
            self.offsets = offsets
        
        def __lt__(self, other):
            return self.offsets[1]-self.offsets[0] < other.offsets[1]-self.offsets[0]

    text = "".join([p, "#", q, "$"])
    tree = dict()
    tree[0] = Node(None, 0, 3, None)
    mode = 1
    ncount = 1
    #highestnode = tree[0]

    for s in range(len(text)):
        currentNode = tree[0]
        #currentText = text[s:]
        curr = (s, len(text))
        #test = text[curr[0]:curr[1]]
        if text[curr[0]] == "#":
            mode = 2
            continue
        while True:
            found = False
            currentText = text[curr[0]:curr[1]]
            for keyS, keyE in currentNode.children.keys():
                pos = -1
                key = text[keyS:keyE]
                for i in range(1, min(len(currentText), len(key))+1):
                    if currentText[:i] == key[:i]:
                        pos = i
                    else:
                        break
                        
                if pos == len(key):
                    found = True
                    currentNode = tree[currentNode.children[(keyS, keyE)]]
                    curr = (curr[0]+pos, curr[1]) #currentText[pos:]
                    if mode == 2 and currentNode.mode < 3:
                        currentNode.mode += 2
                    break
                elif pos != -1:
                    found = True
                    subA = (keyS, keyS+pos)
                    subB = (keyS+pos, keyE)

                    # create new node with second part of old string
                    currentNode.children[subA] = ncount
                    if mode == 2 and currentNode.mode < 3:
                        currentNode.mode += 2

                    tree[ncount] = Node(currentNode, currentNode.rank+1, 1, subA)
                    tree[ncount].children[subB] = currentNode.children[(keyS, keyE)]

                    # set correct mode
                    if mode == 2 and tree[ncount].mode == 1:
                        tree[ncount].mode += 2

                    # fix parent
                    tree[currentNode.children[(keyS, keyE)]].parent = tree[ncount]
                    tree[currentNode.children[(keyS, keyE)]].offsets = subB

                    # add second part of new string
                    tree[ncount].children[(curr[0]+pos, curr[1])] = ncount + 1

                    # create new node for the new string
                    tree[ncount+1] = Node(tree[ncount], tree[ncount].rank+1, mode, (curr[0]+pos, curr[1]))
                    ncount += 2

                    currentNode.children.pop((keyS, keyE), None)
                    currentText = None
                    break

            if not found:
                currentNode.children[curr] = ncount
                tree[ncount] = Node(currentNode, currentNode.rank+1, mode, curr)
                ncount += 1
                break
            elif not currentText:
                break
    
    # find shortest sequence
    result = ""
    h = []
    heapq.heappush(h, (0, tree[0]))
    counter = 0
    while h:
        cnt, currentNode = heapq.heappop(h)
        counter += 1
        for idx in currentNode.children:
            childNode = tree[currentNode.children[idx]]
            if childNode.mode == 1 and text[childNode.offsets[0]] != "#":
                # if found, reconstruct string and exit
                result = text[childNode.offsets[0]]
                while currentNode.offsets:
                    subtext = text[currentNode.offsets[0]:currentNode.offsets[1]]
                    result = ''.join([subtext, result])
                    currentNode = currentNode.parent
                # clear heap to exit
                h.clear()
                break
            elif childNode.mode == 3:
                childcnt = childNode.offsets[1] - childNode.offsets[0]
                heapq.heappush(h, (cnt+childcnt, childNode))
    
    return result


if __name__ == "__main__":
	p = sys.stdin.readline().strip()
	q = sys.stdin.readline().strip()
	ans = solve(p, q)
	sys.stdout.write(ans + '\n')