import numpy as np
grafo = []
dados = []
vertice = list()
C = []
A = []


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
    print(lista)
    i = lista[0]
    nn = 0
    shorter_dist = float('Inf')
    total_dist = 0
    while len(C) != dimension:
        for j in lista:
            ver1 = np.array(i)
            if j not in C:
                ver2 = np.array(j)  # passa por todos os k vertices
                calc = np.linalg.norm(ver1 - ver2)  # realiza o calcula da distancia de atual  e K
                if calc <= shorter_dist:
                    shorter_dist = calc
                    nn = j

        C.append(nn)
        print(C)
        i = nn
        total_dist += shorter_dist
        shorter_dist = float('Inf')

    ver3 = np.array((C[-1]))
    ver4 = np.array(lista[0])
    last_one = np.linalg.norm(ver3 - ver4)
    Solucao = total_dist + last_one

    return Solucao

def improvement(C):
    best = 0
    i = 0
    while i < dimension -2:
        C[i], C[i + 1] = C[i], C[i + 1]
        melhorada = closer(C)
        print(melhorada)
        i += 1
        if melhorada <= trivial:
            best = melhorada
    return best



name = input()
comment = input()
tipo = input()
dimension = input()
test1 = input()
test2 = input()
dimension = int(float((dimension[dimension.find(':') + 2:])))
vertex(dimension)


trivial = closer(vertice)
print(f'Solução Trivial: {trivial}')

melhorada = improvement(C)
print(f'Solução melhorada: {melhorada}')


