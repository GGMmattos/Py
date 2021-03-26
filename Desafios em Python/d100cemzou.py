#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
#  a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep
numeros = list()

def sortear():
    print(20* "=-")
    print("Sorteando 5 valores da lista ", end=" ")
    for i in range (0,5):
        n1 = randint(0,10)
        numeros.append(n1)
        print(F'{n1}', end=" ", flush=True)
        sleep(0.5)
    print(' PRONTO!')

def somaPar(list) :
    soma=0
    for i in list:
        if i % 2 == 0:
            soma += i 
    print(f"Somandos os valores pares de {numeros}, temos {soma}")

sortear()
somaPar(numeros)
