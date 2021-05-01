#GAME: pedra, papel, tesoura

from time import sleep
from random import randint
escolha= ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''
Suas Opções:

0 *PEDRA
1 *PAPEL
1 *TESOURA

''')
jogada=int(input("Qual é a sua jogada?"))
print("\n")
print('-='*12)
print('Computador jogou {}'.format(escolha[computador]))
print('Jogador jogou {}'.format(escolha[jogada]))
print('-='*12)
print('\n')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO\n')
sleep(1)

if computador == 0:  #pedra
    if jogada == 0:
        print('EMPATOU')
    elif jogada == 1:
        print('JOGAR GANHOU')
    elif jogada == 2:
        print('COMPUTADOR GANHOU')
elif computador == 1: # pepel
    if jogada == 1:
        print("EMPATOU")
    elif jogada == 0:
        print('COMPUTADOR GANHOU')
    elif jogada == 2:
        print('JOGADOR GANHOU')
elif computador == 2:  #tesoura
    if jogada == 2:
        print("EMPATOU")
    elif jogada == 0:
        print("JOGADOR GANHOU")
    elif jogada == 1:
        print('COMPUTADOR GANHOU') 
