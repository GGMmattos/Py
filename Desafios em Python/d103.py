#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
#o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
#mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=0, gols=0):
    if nome == "":
        nome = "<desconhecido>"

    print(f"O jogador {nome} fez {gols} gol(s)")

name = str(input("Qual o nome do jogador? "))
gols = str(input("Quantos gols ele marcou? "))
if gols.isnumeric():  #Verifica se o numero ou uma string
    gols = int(gols)
else:
    gols=0
ficha(name,gols)