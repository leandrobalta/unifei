# Função: Busca em Largura
# Descrição: Obtém a sequência dos vértices visitados conforme a Busca em Largura (Breadth First Search, BFS).
# Entrada: lista de adjacências (Dictionary)
# Saída: Lista de inteiros com a sequência dos vértices visitados (List [Integer])

def BFS(graph, start):
    visited = []
    analyzed = []
    visited.append(start)
    
    
    while len(visited) > 0:
        node = visited.pop(0);
    
        for item in graph[node]:
            if not item in visited and not item in analyzed:
                visited.append(item)
            
        analyzed.append(node)
        
        
        
    for item in graph:
        if not item in analyzed:
            analyzed.append(item)
            
    return print(analyzed)
            
        
BFS({0: [2, 4], 1: [2, 4], 2: [0, 1, 4], 3: [], 4: [0, 1, 2, 5, 6], 5: [4, 6], 6: [4, 5]}, 0);