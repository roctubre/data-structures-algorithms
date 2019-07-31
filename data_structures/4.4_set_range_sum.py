# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
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

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key): 
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v        
        last = v
        if v.key == key:
            break        
        if v.key < key:
            v = v.right
        else: 
            v = v.left            
    root = splay(last)
    return (next, root)

def split(root, key):    
    (result, root) = find(root, key)    
    if result == None:        
        return (root, None)    
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)

    
def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right

    
# Code that uses splay tree to solve the problem

root = None

def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)    
    root = merge(merge(left, new_vertex), right)
    
def erase(x): 
    global root
    
    # find key, return if not found
    (result, root) = find(root, x)
    if not result or (result and result.key != x):
        return
    
    # put parent, then searched node to top
    splay(result.parent)
    splay(result)
    
    # get left and right subtrees
    l = result.left
    r = result.right
    
    # remove seached node as parent from both subtrees and merge them
    if l:
        l.parent = None
    if r:
        r.parent = None
    root = merge(l, r)

        
def search(x): 
    global root
    
    # find key and if found return true
    (result, root) = find(root, x)
    if result and result.key == x:
        splay(result)
        return True
            
    return False
    
    
def sum(fr, to): 
    global root
    
    # return 0 if no tree 
    if not root:
        return 0
            
    # switch values of 'fr' and 'to' if order is not ascending
    if fr > to:
        fr, to = to, fr
    
    # split tree into 3 parts
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    ans = 0
 
    # set to middle.sum if tree was able to be split into a mid part
    # if mid part not existing, it is either the left split or right split
    # since the right split is outside of the searched range, the sum must be 0
    if middle:
        ans = middle.sum
    elif left and left.key >= fr:
        ans = left.sum
    
    # merge subtrees back together
    right = merge(middle, right)
    root = merge(left, right)
    update(root)

    return ans

    
if __name__ == "__main__":
    MODULO = 1000000001
    n = int(stdin.readline())
    last_sum_result = 0
    for i in range(n):
        line = stdin.readline().split()
        if line[0] == '+':
            x = int(line[1])
            insert((x + last_sum_result) % MODULO)
        elif line[0] == '-':
            x = int(line[1])
            erase((x + last_sum_result) % MODULO)
        elif line[0] == '?':
            x = int(line[1])
            print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
        elif line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
            print(res)
            last_sum_result = res % MODULO