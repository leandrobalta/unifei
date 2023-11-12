def prim(matrix):
    v = 0
    selected = [v]
    not_selected = []
    tree = []
    
    for i in range(len(matrix)):
        if i == v:
            continue
        not_selected.append(i)
    
    while len(tree) < len(matrix) - 1:
        adj_dict = {}
        for i in range(len(matrix[v])):
            print(f"matrix[v][i]: {matrix[v][i]}")
            if matrix[v][i] > 0 and i in not_selected:
                print("inside if")
                adj_dict[i] = matrix[v][i]
                
        key_list = list(adj_dict.keys())
        val_list = list(adj_dict.values())
        print(f"key list {key_list}")
        print(f"val list {val_list}")
 
        position = val_list.index(min(val_list))
        
        min_adj_vertex = key_list[position]
        selected.append(min_adj_vertex)
        not_selected.remove(min_adj_vertex)
        tree.append((v, min_adj_vertex))

    print(tree)

prim([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])


# [(0, 1), (0, 7), (7, 6), (6, 5), (5, 2), (2, 8), (2, 3), (3, 4)] 37
