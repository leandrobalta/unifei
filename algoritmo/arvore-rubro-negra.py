#Leandro Braga - 2022004260
#João Leão Guedes Filho - 2021017110

class noh:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        self.cor = True

def rotacionaEsquerda(y):
    x = y.dir
    y.dir = x.esq
    x.esq = y
    x.cor = y.cor
    y.cor = True
    return x


def rotacionaDireita(y):
    x = y.esq
    y.esq = x.dir
    x.dir = y
    x.cor = y.cor
    y.cor = True
    return x

def sobeVermelho(y):
    y.cor = True
    y.esq.cor = False
    y.dir.cor = False

def ehVermelho(y):
    if y == None:
        return False
    else:
        return y.cor

def ehNegro(y):
    if y == None:
        return True
    else:
        return y.cor == False


def insere_aux(raiz, dado):
    if raiz == None:
        return noh(dado)
    elif dado < raiz.dado:
        raiz.esq = insere_aux(raiz.esq, dado)
    elif dado > raiz.dado:
        raiz.dir = insere_aux(raiz.dir, dado)
    else:
        #jah existe esse dado, ignorar
        return raiz

    if ehVermelho(raiz.dir) and ehNegro(raiz.esq):
        raiz = rotacionaEsquerda(raiz)
    if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
        raiz = rotacionaDireita(raiz)
    if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
        sobeVermelho(raiz)
    return raiz

def insere(raiz, dado):
    raiz = insere_aux(raiz, dado)
    raiz.cor = False
    return raiz

def busca(raiz, dado):
    if raiz == None:
        return f"{dado} nao encontrado"
    
    if dado < raiz.dado.split(' ')[0]:
        return busca(raiz.esq, dado)
    if dado > raiz.dado.split(' ')[0]:
        return busca(raiz.dir, dado)
    
    return " ".join(raiz.dado.split(' ')[1:])

def min(arvore):
    if arvore == None:
        return

    if arvore.esq == None:
        print(arvore.dado)
    
    min(arvore.esq)

def max(arvore):
    if arvore == None:
        return

    if arvore.dir == None:
        print(arvore.dado)
    
    max(arvore.dir)

tree = None

while True:
    entry = input()

    if entry == "i":
        insert_item = input()
        tree = insere(tree, insert_item)
        continue

    if entry == "b":
        search_item = input()
        print(busca(tree, search_item))
        continue

    if entry == "min":
        min(tree)
        continue

    if entry == "max":
        max(tree)
        continue

    if entry == "x":
        break
    
    else:
        print("comando nao identificado, tente novamente...")
        continue
