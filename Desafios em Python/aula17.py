num = [1,3,5,6,7,8]

#listas são mutáveis
num[2]  = 12
print(num)

#adicionar um novo elemesnto na lista, no final

num.append(7)
print(num)

#ordena uma lista
num.sort()
print(num)

#ordena  na ordem reversa
num.sort(reverse=True)
print(num)
#numero de elementos
len(num)

#adicionando um elemento em um ugar x
#colocando o 2 na posição 0 como exemplo
num.insert(2,0)

#remoção de elementeos

#remover ultima posição da lista
num.pop()
print(num)
#remove oela primeira ocorrencia de um dados caso tenha valor igual
num.remove(3)

for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')
print("Ufa, cheguei ao fim")

#criando uma lista e ppassando valores para a mesma com um laço FOR
exemplo = list()
for cont in range (0,5):
    exemplo.append(int(input("Digite um valor: ")))


