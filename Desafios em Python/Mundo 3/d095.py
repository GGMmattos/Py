#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
gols = list()
time = list()

while True:
    jogador.clear() #limpa os dados a cada laço q atribuimos um jogador
    jogador['nome'] = str(input("Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou?: "))
    gols.clear()
    for c in range(0,partidas):
        gols.append(int(input(f"Quantos gols na {c+1} partida? ")))

    jogador['gols'] = gols[:]  #copia da lista 'gols'
    jogador['total'] = sum(gols)   #somas de todos elementos contidos na lista...
    time.append(jogador.copy())

    while True:
        esc = str(input("Deseja continuar? ")).upper()[0]
        if esc  in 'SN':
            break
        print("ERROR!!! por favor, responda somente S ou N")
    if esc == 'N':
        break
print(45*"-")

print('cod ', end='')

for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print(45*"-")

for k,v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print(45*"-")

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print("ERRO!!!, Não existe jogador com esse código")
    else:
        print(f"  --LEVANTAMENTO DO JOGADOR {time[busca]['nome']}")
        for i,g in enumerate(time[busca]["gols"]):
            print(f" No jogo {i+1} fez {g} gols")
    print(40*"-")
    
print("programa finalizado")





