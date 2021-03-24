 #Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
 #O programa vai ler o nome do jogador e quantas partidas ele jogou. 
 #Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
 #incluindo o total de gols feitos durante o campeonato.'''

jogador = dict()
gols = list()

jogador['nome'] = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?"))
for c in range(0,partidas):
    gols.append(int(input(f"Quantos gols na {c+1} partida? ")))
jogador['gols'] = gols[:]  #copia da lista 'gols'
jogador['total'] = sum(gols)   #somas de todos elementos contidos na lista...

print(jogador)
print(20*'=-')

for k,v in jogador.items():
    print(f"O campo  {k} tem valor  {v}")
print(20*'=-')
print(f"O jogador {jogador['nome']} jogou {len(gols)} partidas")
for i,v in enumerate(gols):
    print(f" => Na partida {i+1} fez {v} gols")
print(f"Foi um total de {jogador['total']} gols ao todo")


