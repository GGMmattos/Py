#Crie um programa onde o usuário possa digitar sete valores numéricos
#e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]



for i in range(1,8):
    n1 =(int(input(f"Informe o {i}º valor: ")))
    print()
    if n1 % 2 ==0:
        lista[0].append(n1)
    else:
        lista[1].append((n1))

print(f'Lista com valores pares digitados: {sorted(lista[0])}')
print(f'Lista com valores impares digitados: {sorted(lista[1])}')
print()
print("Fim do programa.")

