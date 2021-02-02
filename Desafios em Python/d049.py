#Mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("informe um numero para fazer a tabuada do mesmo > "))

for i in range (0,11):
    print(' {} X {:2} > {}'.format(num,i, num*i))