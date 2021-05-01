#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 =float(input("Informe um numero: "))

n2 =float(input("Informe outro numero: "))

n3 =float(input("Informe um ultimo numero: "))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = 1

if n2 > n1 and n2 > n3:
    maior = n2
if  n3 > n1 and n3 > n2:
    meio = n3

print("O menor valor é {}".format(menor))

print("O maior valor é {}".format(maior))
