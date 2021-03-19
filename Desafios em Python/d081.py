#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
while True:
    escolha = " "
    lista.append(int(input("Informe um número: ")))
    escolha = str(input(("Deseja continuar?[S/N]: "))).upper()
    if escolha in 'N':
        break
print(20*'=-')
print(f"Total de numeros digitados: {len(lista)}")
lista.sort(reverse=True)
print(f"Valores ordenados de forma decrescente: {lista}")
if 5 in lista:
    print("O valor 5 está na lista")
else:
    print("O valor 5 não está na lista")


