#   Aluno: Leandro Balta Braga
#   Matricula: 2022004260

import numpy as np
    
def isSymmetric(matriz):
    if np.tril(matriz).sum() != np.triu(matriz).sum():
        return False
    
    return True

def hasLoop(matriz):
    if np.diag(matriz).sum() > 0: 
        return True
        
    return False

def isSimpleGraph(matriz):  
    isSimple = True
    
    if not isSymmetric(matriz):
        isSimple = False
    
    if np.diag(matriz).sum() != 0:
        isSimple = False
    
    return isSimple

def isDirectedGraph(matriz):
    isDirected = True
    
    if np.diag(matriz).sum() != 0:
        isDirected = False
        
    if isSymmetric(matriz):
        isDirected = False
    
    return isDirected

def isMultiGraph(matriz):
    isMulti = True
    
    if not isSymmetric(matriz):
        isMulti = False
    
    if np.diag(matriz).sum() > 0: 
        isMulti = False
        
    parallel = False
        
    for i in range(matriz):
        for j in range(matriz[i]):
            if matriz[i][j] > 1:
                parallel = True
    
    if not parallel:
        isMulti = False     
    
    return isMulti

def isDirectedMultiGraph(matriz):
    isDirectedMulti = True
    
    if isSymmetric(matriz):
        isDirectedMulti = False
    
    if np.diag(matriz).sum() > 0: 
        isDirectedMulti = False
        
    parallel = False
        
    for i in range(matriz):
        for j in range(matriz[i]):
            if matriz[i][j] > 1:
                parallel = True
    
    if not parallel:
        isDirectedMulti = False     
    
    return isDirectedMulti   


def isPseudoGraph(matriz):
    isPseudo = True
    
    if not isSymmetric(matriz):
        isPseudo = False
        
    if not hasLoop(matriz): 
        isPseudo = False
        
    parallel = False
        
    for i in range(matriz):
        for j in range(matriz[i]):
            if matriz[i][j] > 1:
                parallel = True
    
    if not parallel:
        isPseudo = False  
        
    return isPseudo

def tipoGrafo(matriz): 
    
    if isSimpleGraph(matriz):
        return print(0)
    
    if isDirectedGraph(matriz):
        return print(1)
    
    if isMultiGraph(matriz):
        return print(20)
    
    if isDirectedMultiGraph(matriz):
        return print(21)
    
    if isPseudoGraph(matriz):
        return print(30)
    
    return print(31)
    
        

def verificaAdjencia(matriz, i, j):
    return 1

def calcDensidade(matriz):
    return 1

def insereAresta(matriz, i, j):
    return 1

def removeAresta(matriz, i, j):
    return 1

def insereVertice(matriz, i):
    return 1

def removeVertice(matriz, i):
    return 1
