def getSources(adjList):
    sources = []
    for key in adjList:
        isSource = True
        for check_key in adjList:
            if key in adjList[check_key]:
                isSource = False
                
        if isSource: 
            sources.append(key)
            
    return sources

    
def isSource(adjList, vertex):
    source = True
    for check_key in adjList:
        if vertex in adjList[check_key]:
            source = False
            
    return source


def getEdgesDirectedGraph(adjList):
    edges = []
    
    for key in adjList:
        for item in adjList[key]:
            edges.append([key, item])
            
    return edges

def ordenacaoTopologicaKahn(adjList):
    thopological_sorted_list = []
    sources = getSources(adjList)
    edges = adjList
        
    while len(sources) != 0:
        removed = sources.pop(0)
        thopological_sorted_list.append(removed)
        removed_bows = edges[removed]
        edges[removed] = []
        for vertex in removed_bows:
            if isSource(edges, vertex):
                sources.append(vertex)
                
    if any(edges.values()):
        return print("NÃO DAG")
    
    return print(thopological_sorted_list)

    
ordenacaoTopologicaKahn({0: [1], 1: [], 2: [0], 3: [1, 2], 4: [1, 2]})