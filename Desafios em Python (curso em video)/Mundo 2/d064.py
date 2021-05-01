# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que 
# é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num=0
n=0
ns=0
while n != 999:
    n = int(input("Informe um numero"))
    n = ns
    ns+=ns
    n=0
    num+=1
print("Você digitou {} numeros, a soma dos mesmo é {}".format(num,ns))