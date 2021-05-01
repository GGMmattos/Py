#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import  sleep

def maior(*valores):
    print(30 *"=-")
    print("Analizando valores passados...")
    maior = 0

    for num in valores:
        if num > maior:
            maior = num
        print(f"{num}", end=" ", flush=True)
        sleep(0.5)
    print(f"Foram informados {len(valores)} valores ao todos")
    print(f"O maior valor informado foi {maior}")

#Alguns valores que usei como exemplo...
maior(1,2,3,4,5)
maior(1,2,5,1,5)
maior(7,1,6,8,24,90)
maior(7,2,7,90,2,1232)


        






