import operator
import random
import numpy as np
import pandas as pd

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

#INICIALIZAÇÃO - Faz o armazenamento dos dados contido no arquivo por fim, cria a lista de vertices
def start(dimensao):
    for i in (range(dimensao)):
        vector = input()
        data = vector.split()
        grafo = [int(data[1]), int(data[2])]
        if i == 'EOF':
            return 0
        else:
            vertices.append(grafo)

#CRIAÇÃO DA POPULAÇÃO INICIAL
def iniciaPopulacao(sizePop, listCity):
    populacao = []

    for i in range(0, sizePop):
        populacao.append(criarRota(listCity))
    return populacao

#CRIAR ROTAS - Cria rotas aleatórias
def criarRota(listCity):
    rota = random.sample(listCity, len(listCity))
    return rota

#FUNÇÃO DE APTIDAO
def fitness(lista):
    return 1 / float(calc(lista))



def rankRotas(lista):
    fitnessResults = {}
    for i in range(0, len(lista)):
        fitnessResults[i] = fitness(lista[i])
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)

def selecao(ranked, eliteSize):
    resultadoSelecao = []

    df = pd.DataFrame(np.array(ranked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.fitness.sum()

    for i in range(0, eliteSize):
        resultadoSelecao.append(ranked[i][0])

        for i in range(0, len(ranked) - eliteSize):
            pick = 100*random.random()
            for i in range(0, len(ranked)):
                if pick <= df.iat[i, 3]:
                    resultadoSelecao.append(ranked[i][0])
                    break
    return resultadoSelecao

#FUNCAO QUE PEGA OS RESULTADO OPTIDOS NA FUNCAO DE SELECAO E PUSCA OS INDIVÍDUOS NA POPULACAO
def encontroPopulacao(pupulation, resultadoSelecao):
    encontroPopulacao = []
    for i in range(0, len(encontroPopulacao)):
        index = resultadoSelecao[i]
        encontroPopulacao.append(pupulation[index])
    return encontroPopulacao

def breed(parent1, parent2):
    filho =[]
    filhop1 = []
    filhop2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent2))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    # Aqui e feita a escolha do subconjunto aleatorio do primeiro pai
    for i in range(startGene, endGene):
        filhop1.append(parent1[i])
    # Se o gene nao existe no primeiro pai, entao pega no segundo pai
    filhop2 = [item for item in parent2 if item not in filhop2]

    filho = filhop1 + filhop2

    return filho

def breedPopulation(population, eliteSize):
    filho = []
    lenght = len(population) - eliteSize
    pool = random.sample(population, len(population))

    #Aqui usaremos o eliotismo novamente para manter as melhores rotas/individuos

    for i in range(0, eliteSize):
        filho.append(population[i])
    #Logo a baixo usamos a funcao de breed mencionada acima ara preencher o resto dos individuos

    for i in range(0, lenght):
        filho = breed(pool[i], pool[len(population)-i-1])
        filho.append(filho)
    return filho

def mutacao(individual, mutationrate):
    for swapped in range (len(individual)):
        if(random.random() < mutationrate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city1
            individual[swapWith] = city2

    return individual



name = input()
comment = input()
tipo = input()
dimension = input()
test1 = input()
test2 = input()
dimension = int(float((dimension[dimension.find(':') + 2:])))
print()

start(dimension)
populacao = iniciaPopulacao(5, vertices)
sla = rankRotas(populacao)

teste = selecao(sla, 5)

print(teste)


print(sla)






