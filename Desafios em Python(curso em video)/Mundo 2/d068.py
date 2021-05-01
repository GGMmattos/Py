# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print("Vamos jogar impar ou par !!!")

while True:
    valor = int(input("Diga um valor: "))
    tipo = " "
    cont = 0
    think = randint(0, 10)
    soma = valor + think

    while tipo not in "PI":

        tipo = str(input("Impar ou par (I/P): ")).strip().upper()[0]
        print(f"Seu valor {valor}, valor do computado {think}, soma dos numeros  {soma}  ", end='')
        print("Deu par" if soma % 2 == 0 else "Deu impar")

    if tipo == 'P':
        if soma % 2 == 0:
            print("Voce Ganhou !!!")
            cont += 11
        else:
            print("Voce perdeu !!!")
            print(f"Voce ganhou {cont} vez ")
            break
    elif tipo == 'I':
        if soma % 2 == 0:
            print("Voce Perdeu !!!")
            print(f"Voce ganhou {cont} vez ")
            cont += 1
            break
        else:
            print("Voce Ganhou !!!")
                

