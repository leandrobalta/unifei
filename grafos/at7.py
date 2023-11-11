current_time = 0


def real_get_vertex_times(adjList, vertex, visited, times_dict):
    global current_time
    
    visited.append(vertex)
    current_time += 1
    times_dict[vertex] = str(current_time)
    
    for node in adjList[vertex]:
        if node not in visited:
            real_get_vertex_times(adjList, node, visited, times_dict);
            
    current_time += 1
    times_dict[vertex] += '/' + str(current_time)

def temposVertices(adjList, vertex):
    visited = []
    times_dict = {}
    
    real_get_vertex_times(adjList, vertex, visited, times_dict)
    
    for key in adjList:
        if key not in visited:
            real_get_vertex_times(adjList, key, visited, times_dict)
    
    return print(dict(sorted(times_dict.items())))        



example = {0: [1, 4], 1: [2, 4], 2: [5], 3: [0, 4], 4: [5], 5: [1]}        
temposVertices(example, 0)