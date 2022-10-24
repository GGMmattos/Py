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
def mais_prox(lista):
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


name = input()
comment = input()
tipo = input()
dimension = input()
test1 = input()
test2 = input()
dimension = int(float((dimension[dimension.find(':') + 2:])))
start(dimension)
factivel = mais_prox(vertices)

print(factivel)
