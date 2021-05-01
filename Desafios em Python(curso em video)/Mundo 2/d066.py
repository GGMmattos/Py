#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a #condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
S=i=0
while True:
    n=(int(input("Informe um número, digite 999 para parar: ")))
    if n == 999:
        break
    S+=n
    i+=1
print(f'Quantidade de números digitados {i}, a soma dos números {S}')