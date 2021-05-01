#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


produtos = ('Teclado', 10.20,'Mouse', 10, 'Monitor', 700, 'placa de video', 800)

print(f'{"Listagen de preços":^40}')

for pos in range (0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end=" ")
    elif pos % 2 == 1:
        print(f'R${produtos[pos]:>5.2f}')