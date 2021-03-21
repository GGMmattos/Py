#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.


matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0, 3):
        matriz[i][j] = (int(input(f"Informe [{i}] [{j}]: ")))

for i  in range (0,3):
    for j in range(0,3):
        print(f"[{matriz[i][j]:^5}]", end="")
    print()



    