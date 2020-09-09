class Graph():

    def __init__(self, vertices_num):
        # number of nodes (an integer)
        self.v = vertices_num
        # (maybe not useful here) : list of nodes from "A0", "A1" ... to "A index (vertices_num - 1)"
        self.nodes = None

    # from adjacency matrix to dictionary
    def adjmat_2_graph(self, adjm):
        res = {}
        length = len(adjm)

        for i in range(length):
          newVer = 'A' + str(i)
          arr = []
          for j in range(len(adjm[i])):
            s = 'A' + str(j)
            if adjm[i][j] == 0:
              continue
            else:
              arr.append((s, adjm[i][j]))
          res[newVer] = arr
        return res
        
    # from dictionary to adjacency matrix
    def graph_2_mat(self, graph):
        matrix = [[0] * self.v for _ in range(self.v)]
        
        for i in graph.items():
            index = int(i[0][1])
            ver = i[1]
            for ver, weight in ver:
                matrix[index][int(ver[1])] = weight
        return matrix
    # from dictionary to adjacency list    
    def graph_2_list(self, graph):
        adjl = [[] for _ in range(self.v)]
        for i in graph.items():
            first = int(i[0][1])
            ver = i[1]
            adjl[first].append(i[0])
            arr = []
            for tup in ver:
                arr.append(tup)
            adjl[first].append(arr)
        return adjl
    # from adjacency list to dictionary
    def list_2_graph(self, lst):
        dic = {}
        for i in lst:
            dic[i[0]] = i[1]
        return dic
    # from adjacency matrix to adjacency list    
    def mat_2_list(self, mat):
        adjl = [[] for _ in range(self.v)]
        for i in range(self.v):
            first = 'A' + str(i)
            adjl[i].append(first)
            index = -1
            arr = []
            for j in mat[i]:
                index += 1
                if j == 0:
                    continue
                arr.append(('A' + str(index), j))
            adjl[i].append(arr)
        return adjl
    # from adjacency list to adjacency matrix
    def list_2_mat(self, lst):
        mat = [[0] * self.v for _ in range(self.v)]
        for i in lst:
            first, ver = i[0], i[1]
            for ver, weight in ver:
                mat[int(first[1])][int(ver[1])] = weight
        return mat
        
    def dfs(self, u, v, path, graph, allPath):
        path = path + [u]
        if u[1] == v[1]:
            allPath.append(path)
            return
        for ver in graph[u]:
            if ver[0] not in path:
                self.dfs(ver[0], v, path, graph, allPath)
            
    # find all path from node start_vertex to node end_vertex
    def find_all_paths(self, graph, start_vertex, end_vertex):
        allPath = []
        
        self.dfs(start_vertex, end_vertex, [], graph, allPath)
        #print(allPath)
        res = []
        for path in allPath:
            st = ''
            for ver in path:
                st += ver + '-'
            res.append(st[:-1])
        #print(res)
        res.sort(key=len)
        return res
