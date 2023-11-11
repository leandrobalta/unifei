file = open("arquivo.txt", "r")

for line in file:
    print(line.replace("\n", ""))

file.close()
#cana mama fino