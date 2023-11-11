def real_dfs(adjList, vertex, visited):
    visited.append(vertex)
    
    for node in adjList[vertex]:
        if node not in visited:
            real_dfs(adjList, node, visited);
            

def DFS(adjList, vertex):
    visited = []
    
    real_dfs(adjList, vertex, visited)
    
    return print(visited)        

example = {0: [1,2,6], 1: [0,3,4], 2: [0,6,7], 3: [1,4,5], 4: [1,3,5], 5: [3,4], 6: [0,2,7], 7: [2,6]}        
DFS(example, 0)