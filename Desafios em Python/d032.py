#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Informe o ano: obs: coloque 0 para analisar o ano atual:'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano de {} é Bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
