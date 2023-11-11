#Leandro Braga - 2022004260
#João Leão Guedes Filho - 2021017110

#cada nÃ³ tem no minimo t filhos
#cada nÃ³ tem no mÃ¡ximo 2t filhos 

import os, sys

path = "./"

class Node:
    def __init__(self):
        self.leaf = True
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, keysNumber):
        self.keysNumber = keysNumber
        self.root = Node()

    #ESSA EH A FUNCAO QUE VOCÃŠ DEVE FAZER
    #VOCE DEVE CARREGAR DOS ARQUIVOS UMA ARVORE QUE 
    #JA EH VALIDA
    #SUGESTAO: FAZER RECURSIVA
    def readFile(self, fileName):
        
        if fileName == "None":
            return None

        file = open(fileName, "r")
        node = Node()
        
        for line in file:
            lineValue = line.replace("\n", "")

            if lineValue != "None":
                node.leaf = False
            else:
                node.leaf = True
                node.children.append(None)     
                continue           

            isFile = os.path.isfile(lineValue)
            
            if not isFile:
                node.keys.append(int(lineValue))
            else:
                childremNode = self.readFile(lineValue)
                node.children.append(childremNode)                

        return node
    
    def loadFile(self, fileName):
        self.root = self.readFile(fileName)

    def search(self, k, x=None):
        if x == None:
            return self.search(k, self.root)
        else:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search(k, x.children[i])
            


B = BTree(2)
B.loadFile("0.tree")
i = int(input())
while(i != -1):
    if(B.search(i) == None):
        print(str(i) + " nao encontrado")
    else:
        print(str(i) + " encontrado")
    i = int(input())