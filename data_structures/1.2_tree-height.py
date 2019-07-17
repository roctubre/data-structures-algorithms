# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node():
    def __init__(self):
        self.children = []
        
    def addChild(self, node):
        self.children.append(node)

class TreeHeight:
        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))
                
        def orderTraversal(self, node, level=1):
            if not node.children:
                return level
            
            maxlvl = level
            for n in node.children:
                maxlvl = max(self.orderTraversal(n, level+1), maxlvl)
            
            return maxlvl     
                
        def compute_height(self):
                nodes = []
                for i in range(self.n):
                    nodes.append(Node())
                    
                for i in range(self.n):
                    p = self.parent[i]
                    if p == -1:
                        root = i
                    else:
                        nodes[p].addChild(nodes[i])
                        
                # Order traversal
                return self.orderTraversal(nodes[root])

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
