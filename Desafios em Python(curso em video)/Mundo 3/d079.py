# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = list()
escolha = ' '
while True:
    n=(int(input("Digite um numero: ")))
    if n not in numeros:
        numeros.append(n)
        print("Numero adicionado com sucesso")
    else:
        print("O numero ja está contido na lista!!!")
    escolha = str(input("Deseja continuar?[S/N] "))
    if escolha in 'Nn': break
numeros.sort()
print(f'Voce digitou os valores {numeros}')




