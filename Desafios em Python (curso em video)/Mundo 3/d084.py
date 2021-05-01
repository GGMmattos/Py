pessoas = list()
dados = list()
while True:
    dados.append(str(input("Informe seu nome: ")))
    dados.append(float(input("Informe seu peso: ")))
    escolha = str(input("Deseja continuar?[S/N]"))

    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior =  dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    if escolha in "Nn":
        break
print(20*'=-')

print(f'Numero de pessoas que foram cadastradas {len(pessoas)}')

print(f' maior peso: ', end="")
for p in pessoas:
    if p[1] ==  maior:
        print(f'{p[0]}', end=" ")

print()

print(f" menor peso: ", end=" ")
for p in pessoas:
    if p[1] ==  menor:
        print(f"{p[0]}", end=' ')





