import numpy as np

class Graph:
    def __init__(self, grid) -> None:
        self.grid = grid
        
    def sumDiag(self):
        return sum(np.diag(self.grid))
    
    def isSymmetric(self):
        if not np.tril(self.grid) == np.triu(grid):
            return False
        
        return True
        
    def isSimple(self):
        if not self.sumDiag() == 0:
            return False
        
        if not self.isSymmetric():
            return False
        
        return True
        
    def typeGraph(self):
        print()
        
        
        
    
    
grid = [[0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 1, 1, 0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 1, 0, 1, 0, 1],
                    [0, 1, 0, 0, 1, 0, 1, 0, 1],
                    [0, 0, 1, 1, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 1, 1, 0],
                    [0, 0, 1, 1, 0, 1, 0, 1, 1],
                    [1, 1, 0, 0, 0, 1, 1, 0, 1],
                    [0, 0, 1, 1, 0, 0, 1, 1, 0]]

graph = Graph(grid)

graph.typeGraph()
