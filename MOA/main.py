import numpy as np

grafo = []
dados = []
vertice = list()


def vertex(dimensao):
    for i in (range(dimensao)):
        vetor = input()
        dados = vetor.split()
        grafo = [int(dados[1]), int(dados[2])]
        if i == 'EOF':
            return 0
        else:
            vertice.append(grafo)


def closer():

    C = []
    i = vertice[0]
    m = 0
    nn = 0
    menorDist = float('Inf')
    Dtotal = 0
    while len(C) != dimensao:
        for j in vertice:
            ver1 = np.array(i)
            if j not in C:
                ver2 = np.array(j)  # passa por todos os k vertices
                calc = np.linalg.norm(ver1 - ver2)  # realiza o calcula da distancia de atual  e K
                if calc < menorDist:
                  menorDist = calc
                  nn =j
        i = nn
        Dtotal += menorDist
        menorDist = float('Inf')
        C.append(i)
    ver3 = np.array((C[-1]))
    ver4 = np.array(vertice[0])
    m = np.linalg.norm(ver3 - ver4)

    return Dtotal + m


name = input()
comment = input()
tipo = input()
dimensao = input()
test1 = input()
test2 = input()
dimensao = int(float((dimensao[dimensao.find(':') + 2:])))
vertex(dimensao)
valor = closer()

print(valor)
