def subtract_array(arr1, arr2):
    result = [ ]
    
    for item1 in arr1:
        if item1 not in arr2:
            result.append(item1)
            
    return result

def get_min(open_vertex, costs):
    costs_arr = []
    for vertex in open_vertex:
        if costs[vertex] != -1 :
            costs_arr.append(costs[vertex])
        
    return min(costs_arr)

def get_min_path(path, source, target):
    ##print(f"get min path , path received: {path}")
    
    min_path = [target]
    helper = path[target]
    min_path.append(helper)
    while helper != source:
        min_path.append(path[helper])
        helper = path[helper]
        
    min_path.reverse()
        
    return min_path
    
def dijkstra(matrix, source, target):
    costs = []
    path = []
    open_vertex = []
    closed_vertex = []
    
    for i in range(len(matrix)):
        costs.append(9999)
        path.append(0)
        open_vertex.append(i)
        
    costs[source] = 0
    
    while len(open_vertex) != 0:
        min_value = get_min(open_vertex, costs)
        index_min_value = costs.index(min_value)
        #print(f"costs: [{costs}]")
        # print(f"open_vertex: [{open_vertex}]")
        # print(f"closed_vertex: {closed_vertex}")
        # print(f"min value in costs: [{min_value}]")
        # print(f"index_min_value: [{index_min_value}]")
        
        closed_vertex.append(index_min_value)
        open_vertex.remove(index_min_value)
            
    
        # print(f"open_vertex after: [{open_vertex}]")
        # print(f"closed_vertex after {closed_vertex}")
        
        n = subtract_array(open_vertex, closed_vertex)
        
        #print(f"n is : {n}\n")
        for u in n:
            if costs[u] > costs[index_min_value] + matrix[index_min_value][u] and matrix[index_min_value][u] != -1: 
                costs[u] = costs[index_min_value] + matrix[index_min_value][u]
                path[u] = index_min_value
                
        #print(f"path: {path}")
        #print()
        
    print(get_min_path(path, source, target), costs[target])
    

dijkstra([[0, 3, 8, 4, -1, 10], [ 3, 0, -1, 6, -1, -1], [ 8, -1, 0, -1, 7, -1], [ 4,  6, -1, 0,  1,  3], [-1, -1,  7,  1, 0, 1], [10, -1, -1,  3,  1, 0]], 0, 5)
