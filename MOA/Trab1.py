import numpy as np

grafo = []
dados = []
vertice = list()
list_aux = []
list_aux1 = []
k_lista = []

def init(dimensao):
    for i in (range(dimensao)):
        vector = input()
        dados = vector.split()
        grafo = [int(dados[1]), int(dados[2])]
        if i == 'EOF':
            return 0
        else:
            vertice.append(grafo)

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
    resp = calc + last_one1
    return resp

def calc_eucli(ver1, ver2):
    a = np.array((ver1))
    b = np.array((ver2))
    dist = np.sqrt(np.sum(np.square(a - b)))

    return dist

def opt(lista):
    min_change = float('Inf')
    k_lista = lista.copy()
    for i in range(len(k_lista) - 2):
        for j in range(i+2, len(k_lista) - 1):
            custo_atual = calc_eucli(k_lista[i], k_lista[i + 1]) + calc_eucli(k_lista[j], k_lista[j + 1])
            custo_novo = calc_eucli(k_lista[i], k_lista[j]) + calc_eucli(k_lista[i + 1], k_lista[j + 1])
            change = custo_novo - custo_atual
            if change < min_change:
                min_change = change
                min_i = i
                min_j = j
    if min_change < 0:
        listaux2 = k_lista[min_i + 1: min_j + 1]
        newList = listaux2[::-1]
        k_lista[min_i + 1: min_j + 1] = newList
        k_lista = k_lista.copy()
    return k_lista

def bestWay(a):
    aux = a
    melhor_caminho = factivel
    while True:
        melhor_list  = opt(aux)
        aux = melhor_list
        melhor_temporario = calc(melhor_list)

        if melhor_temporario < melhor_caminho:
            melhor_caminho = melhor_temporario
        else:
            return melhor_caminho


name = input()
comment = input()
tipo = input()
dimension = input()
test1 = input()
test2 = input()
dimension = int(float((dimension[dimension.find(':') + 2:])))
init(dimension)
factivel = mais_prox(vertice)
print(bestWay(a))


