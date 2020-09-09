class Node:
    def __init__(self, nd, parent):
        self.nd = nd
        self.parent = parent
        self.visited = False

def find_shortest_path(grid, start_node, end_node):
    import collections as col
    if start_node is None or end_node is None:
        return []
    if len(grid) == 1 and len(grid[0]) == 1:
        return [start_node]
    startX, startY = start_node.position.x, start_node.position.y
    finishX, finishY = end_node.position.x, end_node.position.y
    
    length = len(grid)
    firstLine = len(grid[0])
    
    parents = [[] * firstLine for _ in range(length)]
    
    for i in range(length):
        p = len(grid[i])
        for j in range(p):
            parents[i].append(Node(grid[i][j], None))
            
    movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    parents[startX][startY].visited = True
    queue = col.deque()
    queue.append(parents[startX][startY])
    
    
    # Used BFS Algorithm
    while queue:
        
        currNode = queue.popleft()
        
        for mv in movement:
            xPos, yPos = currNode.nd.position.x, currNode.nd.position.y
            if -1 < xPos + mv[0] < length and -1 < yPos + mv[1] < len(grid[xPos]) and currNode.nd.passable: 
                if not parents[xPos + mv[0]][yPos + mv[1]].visited:
                    parents[xPos + mv[0]][yPos + mv[1]].parent = currNode
                    parents[xPos + mv[0]][yPos + mv[1]].visited = True
                    queue.append(parents[xPos + mv[0]][yPos + mv[1]])
                    
    n = parents[finishX][finishY]
    result = []
    
    while n is not None:
        result.append(n.nd)
        n = n.parent
    
    return result[::-1]