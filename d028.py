#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from  random import  randint
from time import sleep
numero = int(input('Informe um numero: '))
print('Processando...')
sleep(3)
escolha=randint(0,5)

if escolha==numero:
    print("Parabéns voce acertou :-) !!!")
else:
    print("Não cara, você errou eu pensei no numero {} e não no  {}".format(escolha, numero))

