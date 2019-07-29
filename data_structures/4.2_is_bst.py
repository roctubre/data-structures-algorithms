#!/usr/bin/python3

import sys, threading
import math

def IsBinarySearchTree(tree):
    stack = []
    valid = True
    
    # append root node to stack
    if tree:
        stack.append([0, -math.inf, math.inf, -1, -1])

    while stack:
        node_idx = stack[-1][0]
        # check if valid node
        if node_idx == -1:
            stack.pop()
            if stack[-1][3] == -1:
                stack[-1][3] = True
            else:
                stack[-1][4] = True
            continue
        # check if node is between min and max
        elif stack[-1][1] > tree[node_idx][0] or stack[-1][2] < tree[node_idx][0]:
            valid = False
            break
        # check if it already went through the left and right side of the tree
        elif stack[-1][3] != -1 and stack[-1][4] != -1:
            result = stack[-1][3] and stack[-1][4]
            if not result:
                valid = False
                break
                
            stack.pop()
            if not stack:
                break
            if stack[-1][3] == -1:
                stack[-1][3] = result
            else:
                stack[-1][4] = result
            continue
        # go through left side of the tree
        elif stack[-1][3] == -1:
            if tree[node_idx][1] != -1 and tree[tree[node_idx][1]][0] >= tree[node_idx][0]:
                valid = False
                break
            stack.append([tree[node_idx][1], stack[-1][1], tree[node_idx][0], -1, -1])
            continue
        # go through right side of the tree
        elif stack[-1][4] == -1:
            if tree[node_idx][2] != -1 and tree[tree[node_idx][2]][0] < tree[node_idx][0]:
                valid = False
                break
            stack.append([tree[node_idx][2], tree[node_idx][0], stack[-1][2], -1, -1])
            continue
    
    return valid

    
if __name__ == "__main__":
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT") 
    