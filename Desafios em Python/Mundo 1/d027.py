#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Informe seu nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é: {} '.format(nome[0]))

print("Seu ultimo nome: {}".format(nome[len(nome)-1]))
