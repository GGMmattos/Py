#Desempacotamento de listas em Python

#Desempacotamento simples
# lista = ["João", "Marcos", "Pedro"]
# #
# # nome1, nome2, nome3 = lista
# #
# # print(nome1)


lista = ["João", "Marcos", "Pedro",1,2,3,4,5,6,7,8,9]

nome1, nome2, nome3, *outra_listas, ultimo_da_lista = lista    #*_ nos valores que não serão utilizados

print(nome1)
print(outra_listas)
print(ultimo_da_lista)
