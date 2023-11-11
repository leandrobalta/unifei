#Leandro Braga - 2022004260
#João Leão Guedes Filho - 2021017110

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root == None:
        return Node(data)
    if root.data > data:
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root


def search(root, searched_item):
    if root == None:
        return f"{searched_item} nao encontrado"

    if root.data == searched_item:
        return f"{searched_item} encontrado"

    if root.data > searched_item:
        return search(root.left, searched_item)

    else:
        return search(root.right, searched_item)


tree = None

while True:
    entry = input()

    if entry == "i":
        insert_item = input()
        tree = insert(tree, insert_item)
        continue

    if entry == "b":
        search_item = input()
        print(search(tree, search_item))
        continue

    if entry == "x":
        break

    else:
        print("comando nao identificado, tente novamente...")
        continue
