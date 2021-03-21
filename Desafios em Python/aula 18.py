test = list()

test.append('Gabriel')
test.append(21)

galera = list()
#tem que ter os colchetes com o : para n ser irgual mas sim uma copia
galera.append(test[:])
test[0] = 'Joaquim'
test[1] = 32
galera.append(test[:])
#print(galera)

#podemos declarar assim tbm

pessoal = [ ['João', 19] , ['Jose', 29], ['Joco', 23], ['Josef', 13]]
print(pessoal)
#para selecionar apenas um indivídio
print(pessoal[1])
#de modo mais específico ainda
print(pessoal[0][0])

#imprimir todos da lista
for pessoa in pessoal:
    print(pessoa)

#pedindo dados do usuários e colocando na lista
manos = list()
dados = list()
for c in range(0,2):
    dados.append(str(input("Informe seu nome > ")))
    dados.append((int(input("Informe sua idade >"))))
    manos.append(dados[:])
    dados.clear()

print(manos)
