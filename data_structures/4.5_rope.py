# python3

import sys

class Node:
    def __init__(self, key, c = 1, l = None, r = None, p = None):
        self.key = key
        self.count = c
        self.left = l
        self.right = r
        self.parent = p

        
def update(v):
    if v == None:
        return
    v.count = 1 + (v.left.count if v.left != None else 0) + (v.right.count if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v
        
        
def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else: 
            grandparent.right = v

            
def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)        
    else: 
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v    
    

def split(rope, idx):    
    result = rope.find(idx)    
    if result == None:        
        return (rope.root, None)    
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

    
def merge(rope, left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    rope.root = right
    return right
    
    
class Rope:
    def __init__(self, s):
        self.s = s
        self.root = Node(0) if len(s) > 0 else None
            
        for i in range(1, len(self.s)):
            n = Node(i, self.root.count+1)
            self.root.parent = n
            n.left = self.root
            self.root = n
            
    def result(self):
        if not self.root:
            return self.s
        
        arr = []
        stack = [[self.root, 0]]
        
        while stack:
            v = stack[-1]
            if not v[0]:
                stack.pop()
                continue
                
            if v[1] == 0:
                v[1] = 1
                stack.append([v[0].left, 0])
                continue
            elif v[1] == 1:
                v[1] = 2
                arr.append(self.s[v[0].key])
                stack.append([v[0].right, 0])
                continue
            else:
                stack.pop()
        
        return ''.join(arr)
    
    def find(self, idx):
        idx += 1
        if idx <= 0 or idx > len(self.s):
            return None
            
        v = self.root
        last = v
        cut = 0
        x = idx
        while v:
            if x == v.count - (v.right.count if v.right else 0) or \
                (x == 1 and not v.left):
                last = v
                break
            elif (v.left and x <= v.left.count) or (x == 1 and v.left):
                v = v.left
            else:
                cut += v.count - (v.right.count if v.right else 0)
                x = idx - cut
                last = v
                v = v.right
                    
        self.root = splay(last)

        return self.root
        
        
    def process(self, i, j, k):
        (left, subtext) = split(self, i)
        self.root = subtext
        if j == len(self.s) - 1:
            right = None
        else:
            (subtext, right) = split(self, (j+1)-i)

        self.root = merge(self, left, right)

        if k == len(self.s)-(j-i+1):
            left = self.root
            right = None
        else:
            (left, right) = split(self, k)

        left = merge(self, left, subtext)
        self.root = merge(self, left, right)
                

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
