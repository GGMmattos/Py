#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
menor=0
maior=0
for i in range (0,5):
    peso=float(input("Informe o peso  da {}º pessoa: ".format(i+1)))
    if i == 0:
        maior = peso
        menor = peso
    if peso < menor:
        menor=peso 
    if peso > maior:
        maior = peso;    

print("Maior peso lido foi de {}Kg ".format(maior))

print("Menor peso lido foi de {}Kg ".format(menor))


