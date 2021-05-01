# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação, depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos','Athetico-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atletico GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da gama', 'Goiás', 'Coritiba', 'Botafogo')

print(20*"=-")
print(f'Lista dos times do Brasileirão {times}')
print(20*"=-")
print(f'Os 5 primeiros são  {times[0:5]}')
print(20*"=-")
print(f'Os 4 ultimos colocados são  {times[-4]}')
print(20*"=-")
print(f"Times em ordem alfabética {sorted(times)}")
print(20*"=-")
print(f"O time são Paulo aparece na {times.index('São Paulo')} posição ")
print(20*"=-")
