#Separando dígitos de um número

numero=int(input('Informe um numero: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10 


print('Unidade:  {}'.format(u))
print('Dezena:   {}'.format(d))
print('Centena:  {}'.format(c))
print('Milhar    {}'.format(m))