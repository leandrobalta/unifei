def prim(matrix):
    v = 0
    selected = [v]
    not_selected = []
    tree = []
    
    for i in range(len(matrix)):
        if i == v:
            continue
        not_selected.append()
    
    while len(tree) < len(matrix) - 1:
        adj_list = []
        for i in range(len(matrix[v])):
            if matrix[v][i] > 0:
                adj_list.append(matrix[v][i])
                
        u = not_selected.index(min(adj_list))

prim([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])
