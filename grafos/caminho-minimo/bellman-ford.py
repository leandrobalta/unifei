def bellmanFord(matrix, source, target):
    costs = []
    path = []
    for v in range(len(matrix)):
        costs.append(999)
        path.append(0)
        
    costs[source] = 0
    
    for iterations in range(len(matrix)):
        for v in range(len(matrix)):
            for u in range(len(matrix[v])):
                if costs[u] > costs[v] + matrix[v][u] and matrix[v][u] != -1:
                    print(f"path: {path}")
                    print(f"matrix[v][u]: {matrix[v][u]}")
                    print(f"PATH: {path}\n")
                    costs[u] = costs[v] + matrix[v][u]
                    path[u] = v
    
    for v in range(len(matrix)):
            for u in range(len(matrix[v])):
                if costs[u] > costs[v] + matrix[v][u] and matrix[v][u] != -1:
                    print(getMinPath(path, source, target))
                    return False
                
    print(f"{getMinPath(path, source, target)} {costs[target]}")
    return True
    

def getMinPath(path, source, target):
    print(f"path: {path}")
    min_path = [target]
    helper = target
    
    while helper != source:
        min_path.append(path[helper])
        helper = path[helper]
        
    min_path.reverse()    
    
    return min_path
    
    
    


matrix_adj = [
                [ 0 , 6, -1,  7, -1], 
                [-1 , 0,  5,  8, -4],
                [-1, -2,  0, -1, -1], 
                [-1, -1, -3,  0,  9], 
                [ 2, -1,  7, -1,  0]
            ] 

bellmanFord([[0,6,-1,7,-1], [-1,0,5,8,-4], [-1,-2,0,-1,-1], [-1,-1,-3, 0,9], [2,-1,7,-1,0]], 0, 4)