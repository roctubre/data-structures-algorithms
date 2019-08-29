# python3
import sys

def BWT(text):
    mat = []
    tlen = len(text)
    for i in range(tlen):
        mat.append(''.join([text[i:], text[:i]]))
    mat.sort()
    result = ""
    for row in mat:
        result = ''.join([result, row[tlen-1]])
    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))