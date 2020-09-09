class Graph:
    def __init__(self):
        self.dict = {
            # 1st arr = reach with no problem
            # 2nd arr = blocked nodes
            
            'A' : [['D', 'B', 'E', 'H', 'F'], [('C', 'B'), ('I', 'E'), ('G', 'D')]],
            'C' : [['B', 'E', 'F', 'D', 'H'], [('A', 'B'), ('I', 'F'), ('G', 'E')]],
            'I' : [['H', 'F', 'E', 'B', 'D'], [('C', 'F'), ('G', 'H'), ('A', 'E')]],
            'G' : [['H', 'F', 'E', 'B', 'D'], [('C', 'E'), ('I', 'H'), ('A', 'D')]],
            
            'B' : [['A', 'E', 'C', 'D', 'F', 'G', 'I'], [('H', 'E')]],
            'F' : [['A', 'E', 'C', 'I', 'B', 'G', 'H'], [('D', 'E')]],
            'H' : [['A', 'C', 'D', 'E', 'F', 'G', 'I'], [('B', 'E')]],
            'D' : [['A', 'B', 'C', 'E', 'G', 'H', 'I'], [('F', 'E')]],
            
            'E' : [['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'], []]
        }

def DFS(node, graph, length, visited):

    if (length == 1): return 1
    
    visited[node] = True
    
    result = 0
    
    for ver in graph.dict[node][0]:
        if visited[ver] == False:
            result += DFS(ver, graph, length - 1, dict(visited))
            
    for (to, bc) in graph.dict[node][1]:
        if ((visited[bc] == True) and (visited[to] == False)):
            result += DFS(to, graph, length - 1, dict(visited))
                    
    
    return result

        
    

def count_patterns_from(firstPoint, length):
    # Your code here!
    
    if (length <= 0 or length > 9): return 0
    
    visited = {
        'A' : False,
        'B' : False,
        'C' : False,
        'D' : False,
        'E' : False,
        'F' : False,
        'G' : False,
        'H' : False,
        'I' : False
    }
    graph = Graph()
    result = DFS(firstPoint, graph, length, dict(visited))
    
    return result