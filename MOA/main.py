import numpy as np

grafo = []
dados = []
vertice = list()
C = []


def vertex(dimensao):
    for i in (range(dimensao)):
        vector = input()
        data = vector.split()
        grafo = [int(dados[1]), int(dados[2])]
        if i == 'EOF':
            return 0
        else:
            vertice.append(grafo)


def closer(lista):
    i = list[0]
    aux = 0

    shorter_dist = float('Inf')
    total_dist = 0
    while len(C) != dimension:
        for j in lista:
            ver1 = np.array(i)
            if j not in C:
                ver2 = np.array(j)  # passa por todos os k vertices
                calc = np.linalg.norm(ver1 - ver2)  # realiza o calcula da distancia de atual  e K
                if calc < shorter_dist:
                    shorter_dist = calc
                    aux = j
        i = aux
        total_dist += shorter_dist
        shorter_dist = float('Inf')
        C.append(i)
    ver3 = np.array((C[-1]))
    ver4 = np.array(lista[0])
    last_one = np.linalg.norm(ver3 - ver4)

    return total_dist + last_one

def improvement(lista):
    #while len(c) != dimension:
    #    for i in lista:
    lista[0], lista[1] = lista[1], lista[0]
    return lista




name = input()
comment = input()
tipo = input()
dimension = input()
test1 = input()
test2 = input()
dimension = int(float((dimension[dimension.find(':') + 2:])))
vertex(dimension)
valor = closer(C)

print(valor)
improvement(C)
print(C)
