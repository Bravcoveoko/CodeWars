import math
from heapq import heappush, heappop

class Node:
    def __init__(self, ancestor, xPos, yPos, distance, weight):
        self.ancestor = ancestor
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.weight = weight
    
    def __gt__(self, other):
        return False

def relax(u, v):
    v.distance = u.distance + u.weight
    v.ancestor = u  

def cheapest_path(t, start, finish):
    startX, startY = start
    finishX, finishY = finish
    length = len(t)
    p = len(t[0])
    matrix = [[] * p for i in range(length)]
    
    # Fill matrix with class Node and fill their attributes
    for i in range(0, length):
        l = len(t[i])
        for j in range(0, l):
            matrix[i].append(Node(None, i, j, math.inf, t[i][j]))
    
    # DOWN | UP | RIGHT | LEFT 
    movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    matrix[startX][startY].ancestor = None
    matrix[startX][startY].distance = 0
    
    # Used Dijkstra algorithm
    startNode = matrix[startX][startY] 
    heap = []
    heappush(heap, (startNode.distance, startNode))
    
    while heap:
        currNode = heappop(heap)[1]
        x, y = currNode.xPos, currNode.yPos
        if (x, y) == (finishX, finishY):
            break
        
        for mv in movement:
            if-1 < currNode.xPos + mv[0] < length and -1 < currNode.yPos + mv[1] < len(t[currNode.xPos]):
                vNode = matrix[currNode.xPos + mv[0]][currNode.yPos + mv[1]]
                if currNode.distance + currNode.weight < vNode.distance:
                    relax(currNode, vNode)
                    heappush(heap, (vNode.distance, vNode))    
    # Create the path
    n = matrix[finishX][finishY]
    result = []
    
    while n.ancestor is not None:
        ance = n.ancestor
        diffX = ance.xPos - n.xPos
        diffY = ance.yPos - n.yPos
        
        if diffX == 1 and diffY == 0:
            result.append("down")
        elif diffX == -1 and diffY == 0:
            result.append("up")
        elif diffX == 0 and diffY == 1:
            result.append("right")
        else:
            result.append("left")
        n = n.ancestor
    
    result.reverse()
    arrLen = len(result)
    for i in range(arrLen):
        if result[i] == "up":
            result[i] = "down"
        elif result[i] == "down":
            result[i] = "up"
        elif result[i] == "right":
            result[i] = "left"
        else:
            result[i] = "right"
    return result
