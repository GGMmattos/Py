import numpy as np

grafo = []
vertices = list()
list_aux = []


def start(dimensao):
    for i in (range(dimensao)):
        vector = input()
        data = vector.split()
        grafo = [int(data[1]), int(data[2])]
        if i == 'EOF':
            return 0
        else:
            vertices.append(grafo)

def iniciaPopulacao(sizePop, listCity):
    populacao = []

    for i in range(0, sizePop):
        populacao.append(criarRota(listCity))
    return populacao







name = input()
comment = input()
tipo = input()
dimension = input()
test1 = input()
test2 = input()
dimension = int(float((dimension[dimension.find(':') + 2:])))
start(dimension)
print(vertices)

