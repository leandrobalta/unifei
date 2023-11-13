def hasCycle(v, u, tree, parent):
    root_v = find(parent, v)
    root_u = find(parent, u)

    if root_v == root_u:
        return True

    union(parent, root_v, root_u)
    return False

def find(parent, i):
    if parent[i] == -1:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    parent[x] = y

def kruskal(matrix):
    edges_dict = {}
    tree = []
    parent = [-1] * len(matrix)
    cost = 0

    for v in range(len(matrix)):
        for u in range(len(matrix[v])):
            if matrix[v][u] != 0:
                key = (v, u)
                edges_dict[key] = matrix[v][u]

    sorted_edges = dict(sorted(edges_dict.items(), key=lambda x:x[1]))
    # print(sorted_edges)
    # print()

    for (v, u) in sorted_edges.keys():
        #print(f"{v} - {u}")
        if not hasCycle(v, u, tree, parent):
            tree.append((v, u))
            cost += matrix[v][u]

    print(tree, cost)

kruskal([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])

#[(6, 7), (2, 8), (5, 6), (0, 1), (2, 5), (2, 3), (0, 7), (3, 4)] 37
#[(6, 7), (2, 8), (5, 6), (0, 1), (2, 5), (2, 3), (0, 7), (3, 4)]

