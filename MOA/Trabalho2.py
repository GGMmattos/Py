import random
import numpy as np

grafo = []
vertices = list()
list_aux = []

#CALC - Dada uma solução com a lista de cidades, realiza o calculo
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

#INICIALIZAÇÃO - Faz o armazenamento dos dados contigo no arquivo por fim, cria a lista de vertices
def start(dimensao):
    for i in (range(dimensao)):
        vector = input()
        data = vector.split()
        grafo = [int(data[1]), int(data[2])]
        if i == 'EOF':
            return 0
        else:
            vertices.append(grafo)

#CRIAR ROTAS - Cria rotas aleatórias
def criarRota(listCity):
    rota = random.sample(listCity, len(listCity))
    return rota

def fitness(lista):
    print(lista)
    return 1 / float(calc(lista[3]))

#CRIAÇÃO DA POPULAÇÃO INICIAL
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
populacao = iniciaPopulacao(5, vertices)

sla = fitness(populacao)
print(sla)




