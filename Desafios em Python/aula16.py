# tuplas variaveis compostas
# as tuplas são imutáis

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Não consigo atribuir valores a tupla a nao ser pela declaração de uma
#print(lanche[3])

#print(lanche[-2])

#print(lanche[1:3])

#print(lanche[:2])

# percorrendo uma tupla com lanço for
#for comida in lanche:
#    print(f"Eu vou comer {comida}")
#print("Comi pra caramba")

#print("OU \n")
# ou
#for c in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[c]}')
#print("Comi pra caramba")

#mostrando a tupla com o numero referente a posição
#for pos, comida in enumerate(lanche):
#    print(f"Eu vou comer {comida} {pos}")
#print(f"Comi pra caramba ")

#ordenação
#print(sorted(lanche))

a = (1,2,5,4)
b = (12, 6,2, 7, 9)
c = a + b
print(sorted(c))
    
# quantas vezes aparece o numero x na tupla
print(c.count(2))

#em qual psição x esta (pega a primeira ocorrencia
print(c.index(2))

#para pegar as demais ocorrencia podemos começar numa posição acima
print(c.index(2,1))

#apagando um tupla
del(c)


