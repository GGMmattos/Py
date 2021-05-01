#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

tentativas = 0
from  random import  randint
from time import sleep

escolha=randint(0,10)
print('''Olá eu sou seu computador
Acabei de pensar em um numero de 0 até 10...
Consegue adivinhar?''')

acertou = False
while not acertou:
    numero = int(input('\n Qual é o seu palpite: '))
    print('Processando...')
    sleep(3)
    if escolha == numero:
        acertou =True
        print("\nParabéns voce acertou :-) !!! Com {} tentativas".format(tentativas))
    else:
        if numero > escolha:
            print("Menos... Tente novamente!!!")
        elif numero  < escolha:
            print("Mais...Tente novamente")
        tentativas += 1 


