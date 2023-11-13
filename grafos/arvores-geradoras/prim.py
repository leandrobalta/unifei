def prim(matrix):
    selected = [0]
    not_selected = []
    tree = []
    cost = 0
    
    for i in range(len(matrix)):
        if i == 0:
            continue
        not_selected.append(i)
    
    while len(tree) < len(matrix) - 1:
        min_edge = None
        
        for v in selected:
            for i in not_selected:
                if matrix[v][i] > 0 and (min_edge == None or matrix[v][i] < matrix[min_edge[0]][min_edge[1]]):
                    #print(f"inside if matrix[{v}][{i}]: {matrix[v][i]}")
                    min_edge = [v, i]
                         
        selected.append(min_edge[1])
        not_selected.remove(min_edge[1])
        tree.append((min_edge[0], min_edge[1]))
        #print(f"selected {selected}")
        #print(f"not_selected {not_selected}")
        #print(f"tree {tree}")
        #print()
        cost += matrix[min_edge[0]][min_edge[1]]

    print(tree, cost)

prim([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])


# [(0, 1), (0, 7), (7, 6), (6, 5), (5, 2), (2, 8), (2, 3), (3, 4)] 37