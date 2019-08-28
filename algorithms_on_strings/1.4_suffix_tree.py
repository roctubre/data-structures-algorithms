# python3
import sys


def suffix_tree(text):
    """
    Build a suffix tree of the string text
    """
    tree = dict()
    tree[0] = dict()
    ncount = 1
    for s in range(len(text)):
        current = tree[0]
        currentText = text[s:]
        while True:
            found = False
            for key in current.keys():
                pos = -1
                for i in range(1, min(len(currentText), len(key))+1):
                    if currentText[:i] == key[:i]:
                        pos = i
                    else:
                        break

                if pos == len(key):
                    found = True
                    current = tree[current[key]]
                    currentText = currentText[pos:]
                    break
                elif pos != -1:
                    found = True
                    subA = key[:pos]
                    subB = key[pos:]

                    # create new node with second part of old string
                    current[subA] = ncount
                    tree[ncount] = dict()
                    tree[ncount][subB] = current[key]

                    # add second part of new string
                    tree[ncount][currentText[pos:]] = ncount + 1

                    # create new node for the new string
                    ncount += 1
                    tree[ncount] = dict()
                    ncount += 1

                    current.pop(key, None)
                    currentText = None
                    break

            if not found:
                current[text[s:]] = ncount
                tree[ncount] = dict()
                ncount += 1
                break
            elif not currentText:
                break

    return tree 

def get_suffixes(text):
    """ 
    Return a list with all of the labels of edges (the corresponding 
    substrings of the text) of the suffix tree
    """
    edges = []
    tree = suffix_tree(text)
    for node in tree:
        for key in tree[node]:
            edges.append(key)
    return edges


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = get_suffixes(text)
    print("\n".join(result))