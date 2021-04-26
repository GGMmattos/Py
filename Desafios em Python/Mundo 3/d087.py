#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
somapar = somater = maior =0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f"informe [{i}][{j}]: "))
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if matriz[i][2]:
            somater += matriz[i][j]

for i in range(0,3):
    if i ==0:
        maior = matriz[1][i]
    elif matriz[1][i] > maior:
        maior = matriz[1][i]

for i in range(0,3):
    for j in range(0,3):
        print(f"[{matriz [i][j]:^5}]",end="")
    print()

print(20*'=-')
print(f"Soma de todos os valores pares: {somapar}")
print(f"Soma de todos os valores da terceira coluna: {somater}")
print(f"Maior valor da segunda linha: {maior}")

