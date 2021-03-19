#Crie um programa que vai ler vários números e colocar em uma lista Depois disso,
#crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = list()
listaP = list()
listaI = list()

while True:
    lista.append(int(input("Informe um numero: ")))
    escolha = str(input("Deseja continuar?[S/N]: "))
    if escolha in 'Nn':
        break
for i in lista:
    if i % 2 == 0:
        listaP.append(i)
    else:
        listaI.append(i)
print(20*'=-')
print(f"A lista completa é {lista}")
print(f"lista com pares é {listaP}")
print(f"lista com impares é {listaI}")
