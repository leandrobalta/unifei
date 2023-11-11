import numpy as np


def caminhoEuleriano(matriz):
    total = 0
    
    for line in matriz:
        if sum(line) % 2 != 0:
                total += 1
            
    if total == 2:
        return print(True)

    
    if total > 2 or total == 1:
        return print(False)
    
    return print(True)
    