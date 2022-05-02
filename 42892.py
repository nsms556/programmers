# 2019 KAKAO BLIND RECRUITMENT > 길 찾기 게임
# https://programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10**6)

class Node :
    def __init__(self, p) -> None:
        self.x = p[0]
        self.y = p[1]
        self.p = p
        self.left = None
        self.right = None

class Binary_Tree :
    def __init__(self) -> None:
        self.root = None

    def insert(self, item) :
        self.root = self._insert(self.root, item)
        
        return self.root != None

    def _insert(self, node, item) :
        if node == None :
            return Node(item)

        if item[0] < node.x :
            node.left = self._insert(node.left, item)
        else :
            node.right = self._insert(node.right, item)

        return node

def preorder(node) :
    visited = []

    if node == None :
        return visited

    visited.append(node.p)

    visited += preorder(node.left)
    visited += preorder(node.right)

    return visited

def postorder(node) :
    visited = []
    
    if node == None :
        return visited

    visited += postorder(node.left)
    visited += postorder(node.right)

    visited.append(node.p)

    return visited

def solution(nodeinfo):
    nodeinfo = list(map(tuple, nodeinfo))
    node_num = {x:i+1 for i, x in enumerate(nodeinfo)}
    nodeinfo.sort(key = lambda x : (x[1], -x[0]), reverse=True)

    roadmap = Binary_Tree()

    for node in nodeinfo :
        roadmap.insert(node)

    pre = [node_num[p] for p in preorder(roadmap.root)]
    post = [node_num[p] for p in postorder(roadmap.root)]

    return [pre, post]

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))