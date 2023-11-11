# João Leão Guedes Filho - 2021017110 
# Leandro Braga - 2022004260 
from ponto import ponto

exitPoint = ponto(-1, -1)

prevPoint = None

isFirst = True

while True:
    
    first, second = input().split(' ') 
    currPoint = ponto(int(first), int(second))

    if currPoint == exitPoint:
        break
    
    if isFirst: 
        isFirst = False
        prevPoint = currPoint
        continue
    
    if currPoint == prevPoint:
        print("igual ao anterior")

    if currPoint < prevPoint:
        print("menor que o anterior")
    
    if currPoint > prevPoint:
        print("maior que o anterior")
    
    prevPoint = currPoint