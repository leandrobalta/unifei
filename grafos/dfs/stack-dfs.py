def DFS(listAdj, vertex):
    visited = []
    stack = []
    
    visited.append(vertex)
    stack.append(listAdj[vertex])
    
    while len(stack) > 0:
        array = stack[-1]
        # print(f"my current stack top : {array}")

        all_array_visited = True
        for item in array:
            if item not in visited:
                all_array_visited = False
                
        if all_array_visited:
            removed = stack.pop()
            # print(f"all visited so i removed {removed} from  my stack")
            if len(stack) == 0:
                break
            array = stack[-1]
            # print(f"so my new stack top is {array}")
    
            
        for item in array:
            if item not in visited:
                # print(f"{item} not visited yet")
                # print(f"so i WILL add {listAdj[item]} in my stack")
                visited.append(item)
                stack.append(listAdj[item])
                break
            # else:
                # print(f"{item} already visited")
                # print(f"so i wont add {listAdj[item]} in my stack")
            
            
        
    for key in listAdj:
        if key not in visited:
            visited.append(key)
            
    print(visited)
            
            
# def DFS(listAdj, vertex):
#     visited = set()
#     stack = [vertex]

#     while stack:
#         current_vertex = stack.pop()
#         if current_vertex not in visited:
#             visited.add(current_vertex)
#             neighbors = [neighbor for neighbor in listAdj[current_vertex] if neighbor not in visited]
#             stack.extend(neighbors)

#     print(list(visited))
            

example = {0: [1, 3, 4], 1: [0, 2], 2: [1], 3: [0], 4: [0, 5], 5: [4]} # expected result [0, 1, 2, 3, 4, 5]
DFS(example, 0)


