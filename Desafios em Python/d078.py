#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = list()

for v in range (0,5):
    valores.append(int(input(f"Digite valores para a lista na posição {v}:")))

print(f"Os valores da lista são os seguintes: {valores}")

print(f'O menor valor da lista é o {min(valores)}  presente nas posições: ', end=" ")
for i, v in enumerate(valores):
    if v == min(valores):
        print(f"{i}", end="...")

print(f'\nO maior  valor da lista é o{max(valores)} presente nas posições: ', end=" ")
for i, v in enumerate(valores):
    if v == max(valores):
        print(f"{i}", end="... ")
