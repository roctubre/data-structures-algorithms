# python3
import sys

def build_trie(patterns):
    tree = dict()
    tree[0] = dict()
    nodecount = 1
    for p in patterns:
        currentNode = tree[0]
        for i in range(len(p)):
            currentSymbol = p[i]
            if currentSymbol in currentNode:
                currentNode = tree[currentNode[currentSymbol]]
            else:
                currentNode[currentSymbol] = nodecount
                tree[nodecount] = dict()
                currentNode = tree[nodecount]
                nodecount += 1

    return tree

def solve (text, n, patterns):
	result = []
	tree = build_trie(patterns)
	for s in range(len(text)):
		currentnode = tree[0]
		symbol = text[s]
		counter = s
		while True:
			if not currentnode:
				result.append(s)
				break
			elif symbol in currentnode and counter != len(text):
				currentnode = tree[currentnode[symbol]]
				if counter+1 < len(text):
					symbol = text[counter+1]
				counter += 1
			else:
				break

	return result

if __name__ == "__main__":
	text = sys.stdin.readline().strip()
	n = int (sys.stdin.readline().strip())
	patterns = []
	for i in range (n):
		patterns += [sys.stdin.readline().strip()]

	ans = solve (text, n, patterns)
	sys.stdout.write (' '.join(map (str, ans)) + '\n')
