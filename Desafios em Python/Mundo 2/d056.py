# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
mais_velho = 0
z = 0
nome_velho = ''
for i in range(1, 5):
    print('{}º PESSOA'.format(i))
    nome = str(input("NOME:")).split()

    idade = int(input("iDADE:"))

    sexo = str(input("SEXO(M/F): "))
    print("\n")

    soma_idade += idade

    if sexo == 'M'  and idade > mais_velho:
        mais_velho = idade

    if mais_velho == idade:
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        z = z + 1

print("Media das idades > {} anos".format(soma_idade / 4))

print("O nome do homem mais velho é {} ".format(nome_velho))

print("{}  mulher(es) que tem menos de 20 anos".format(z))

