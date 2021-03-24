#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
#  guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#  No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade
#  C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

individuo = dict()
pessoas = list() 
soma = media = 0 

while True:
    individuo.clear() #APAGA A PESSOA ANTERIOS PRA N DAR CONFLITO
    individuo['nome'] = str(input("nome: "))
    while True:
        individuo['sexo'] = str(input("sexo [M/F]: ")).upper()[0]
        if individuo['sexo'] in 'MF':
            break
        print("Erro!!! por favor, informe M ou F") 

    individuo['idade'] = int(input("idade: "))
    soma += individuo['idade']

    pessoas.append(individuo.copy()) #DADOS DO DICIONÁRIO É ATRIBUIDO NA LISTA
    
    while True:
        esc = str(input("Deseja continuar?[S/N]")).upper()[0]
        if esc in "SN":
             break
        print("ERRO!!! Por favor, informe apenas S ou N ")
    if esc == 'N':
        break

print(20 *"=-")

print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas ")
aux = len(pessoas)
media = soma / aux
print(f"B) Média das idades: {media:5.2f} anos")
print(20 *"=-")

print("C) As mulheres cadastradas foram: ", end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f"{p['nome']}; ", end=' ')
print(20 *"=-")
print()
print("D) Lista das pessoas que estão com a idade acima da média: ", end="")

for p in pessoas:
    if p['idade'] > media:
        print("  ",end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end= "")
        print()
        

#print(individuo)
#print(pessoas)