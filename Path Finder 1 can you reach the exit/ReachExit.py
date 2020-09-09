from collections import deque
def path_finder(maze):
    parsed = maze.split("\n")
    length = len(parsed)
    
    visited = [[False] * length for _ in range(length)]
    
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    
    
    while(queue):
        tu = queue.popleft()
        print(tu)
        if (tu[0] == length - 1 and tu[1] == length - 1):
            return True
        movement(queue, tu, length, parsed, visited)
    return False
        
        
def movement(queue, tuple, length, parsed, visited):
    x = tuple[0]
    y = tuple[1]
    
    # UP, DOWN, LEFT, RIGHT
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(4):
        try:
            if -1 < x + move[i][0] < length:
                if -1 < y + move[i][1] < length:
                    if not visited[x + move[i][0]][y + move[i][1]]:
                        visited[x + move[i][0]][y + move[i][1]] = True
                        if parsed[x + move[i][0]][y + move[i][1]] == '.':
                            queue.append((x + move[i][0], y + move[i][1]))
        except:
            continue
  