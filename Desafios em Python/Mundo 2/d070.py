
total = totmil = menor = cont = 0
barato = " "
while True:
    nome=str(input("Nome do produto: "))
    preco=float(input("Preço: R$"))
    total+= preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato =  nome

    escolha = " "

    while escolha not in "SN":
        escolha=str(input("Deseja continuar? (SIM / NÃO")).strip().upper()[0]

    if escolha == 'N':
        break
    cont=cont+1
    
print(f"O total da compra foi {total:.2f}")
print(f"Temos {totmil} produtos custando mais de RS1000,00 reais")
print(f'O produto mais barato foi {barato} que custa  {menor:.2f}')