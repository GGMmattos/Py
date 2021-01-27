#sorteando um item da lista

import random
n1=input('Primeiro aluno: ')
n2=input('Segundo aluno: ')
n3=input('Terceiro aluno: ')
n4=input('Quarto aluno: ')

lista = [n1,n2,n3,n4]

escolha= random.choice(lista)

print("O aluno escolhido {} ".format(escolha))