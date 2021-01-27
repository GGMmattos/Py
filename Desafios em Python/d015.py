#Aluguel de carros

dias=float(input('Quantidade de dias que o carro foi alugado > '))

km=float(input('Quantidade de KM percorrida: '))

dim_dia= dias * 60

dim_km = km * 0.15 #poderia ser tudo em apenas uma linha rrsrs  


preço=dim_dia+dim_km

print('Valor a pagar {}'.format(preço))