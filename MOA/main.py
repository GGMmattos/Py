import numpy as np
from itertools import permutations

grafo = []
dados = []
vertice = list()
list_aux = []
list_aux1 = []


def vertex(dimensao):
    for i in (range(dimensao)):
        vector = input()
        dados = vector.split()
        grafo = [int(dados[1]), int(dados[2])]
        if i == 'EOF':
            return 0
        else:
            vertice.append(grafo)

def closer(lista):
    global a
    i = lista[0]
    nn = 0
    shorter_dist = float('Inf')
    total_dist = 0
    while len(list_aux) != dimension:
        for j in lista:
            ver1 = np.array(i)
            if j not in list_aux:
                ver2 = np.array(j)  # passa por todos os k vertices
                calc = np.linalg.norm(ver1 - ver2)  # realiza o calcula da distancia de atual  e K
                if calc <= shorter_dist:
                    shorter_dist = calc
                    nn = j
        list_aux.append(nn)
        i = nn
        total_dist += shorter_dist
        shorter_dist = float('Inf')

    a = list_aux.copy()
    ver3 = np.array((list_aux[-1]))
    ver4 = np.array(lista[0])
    list_aux.clear()
    last_one = np.linalg.norm(ver3 - ver4)
    Solucao = total_dist + last_one
    return Solucao

def calc(sol):
    calc = 0
    j = 0
    while j < dimension - 1:
            ver1 = np.array(sol[j])
            ver2 = np.array(sol[j + 1])  # passa por todos os k vertices
            calc += np.linalg.norm(ver1 - ver2)  # realiza o calcula da distancia de atual  e K
            j += 1
    ver3 = np.array((sol[-1]))
    ver4 = np.array(sol[0])
    last_one1 = np.linalg.norm(ver3 - ver4)
    resp = calc +last_one1
    return resp

def opt(a):
    perm = permutations(a)
    melhor = 0
    for i in list(perm):
        aux = calc(i)
        if aux < trivial:
            melhor = aux
    return melhor

name = input()
comment = input()
tipo = input()
dimension = input()
test1 = input()
test2 = input()
dimension = int(float((dimension[dimension.find(':') + 2:])))

vertex(dimension)
trivial = closer(vertice)
melhora = opt(a)
print(f'{melhora}')
