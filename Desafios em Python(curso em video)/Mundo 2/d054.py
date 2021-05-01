# Crie um programa que leia o ano de nascimento de um numero N de pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maior=0
menor=0
atual=date.today().year

choice=(int(input("Informe o numero de pessoas deseja analizar > ")))
for i in range(0, choice):
    ano= (int(input("Digite o ano que a {}º pessoa nasceu >".format(i+1))))
    idade = atual - ano
    if(idade >= 21):
        maior+=1
    else:
        menor+=1

print('\nAo todo tivemos {} pessoas maiores de idade'.format(maior)) 
print('E também tivemos {} pessoas menores de idade'.format(menor))