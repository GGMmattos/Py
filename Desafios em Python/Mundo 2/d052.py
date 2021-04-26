#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num=int(input("Informe um nÚmero: "))
total=0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end="") #se divisível azul
        total+=1
    else:
        print('\033[31m', end="") #se não divisivel vermelho
    print('{}'.format(c), end=' ')
print('\n\033[mO nÚmero {} foi divisível {} vez(es)'.format(num,total))

if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')