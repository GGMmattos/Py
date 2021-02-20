#Crie um programa que leia dois valores e mostre um menu na tela:

from time import sleep
n1 = int(input("Informe um valor: "))
n2 = int(input("Informe o segundo valor: "))
escolha=0

while escolha != 5:
    print(''' [1] Soma
 [2]Multiplicar
 [3]maior
 [4]Novos Números
 [5]Sair do programa''' )
    escolha = int(input('Qual é a sua escolha? '))
    if escolha == 1:
        calc = n1+n2
        print("O resultado de  {} + {} é {}\n".format(n1,n2,calc))
    elif escolha ==2:
        calc = n1*n2
        print("O resultado de  {} * {} é {}\n".format(n1,n2,calc))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\nO maior numero entre {} e {} é {}'.format(n1, n2, maior))
    elif escolha == 4:
        print("OK Informe os novos numeros: ")
        n1 = int(input("primeiro valor >  "))
        n2 = int(input("Segundo valor > "))
    elif escolha == 5:
        print("Finalizando...")
    else:
        print("Opção Inválida") 
    sleep(1)
print("\nPrograma Finalizado!!!")


