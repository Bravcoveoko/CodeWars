from heapq import heappush, heappop
class Node:
    def __init__(self, distance, height, xPos, yPos):
        self.distance = distance
        self.height = height
        self.xPos = xPos
        self.yPos = yPos
    def __gt__(self, other):
        return False

def path_finder(area):
  sText = area.split("\n") 
  length = len(sText)
    
  matrix = [[] for _ in range(length)]
    
  for i in range(length):
      for j in range(length):
          matrix[i].append(Node(float('inf'), int(sText[i][j]), i, j))
    
  matrix[0][0].distance = 0
  movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  heap = []
  heappush(heap, (matrix[0][0].distance, matrix[0][0]))
  
  # Dijkstra algorithm
  while heap:
      currNode = heappop(heap)[1]

      if (length - 1, length - 1) == (currNode.xPos, currNode.yPos):
        break

      for mv in movement:
          xP, yP = currNode.xPos, currNode.yPos
          if -1 < xP + mv[0] < length and -1 < yP + mv[1] < length:
              vNode = matrix[xP + mv[0]][yP + mv[1]]
              newDis = abs(vNode.height - currNode.height)
              
              if newDis + currNode.distance < vNode.distance:
                  vNode.distance = newDis + currNode.distance
                  heappush(heap, (vNode.distance, vNode))
  return matrix[length - 1][length - 1].distance