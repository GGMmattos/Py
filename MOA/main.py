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
  distTotal = 0
  C =[]
  atual = vertice[0]
  menorDist = 10000000

  while len(C) != dimensao:
    for k in vertice:
      if k not in C:
        ver1 = np.array((atual))
        ver2 = np.array(k)
        calc = np.linalg.norm(ver1 - ver2)
        if calc < menorDist:
          menorDist = calc
          atual = k

    distTotal = distTotal + menorDist
    C.append(atual)
  return distTotal


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