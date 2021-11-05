
    #Zip - unindo iteráveis: O numero de elemetos se limita a menor lista, quando não sabemos a quantidade de valores
    #Zip_longest - Intertools

from itertools import zip_longest, count

indice = count()
cidade = ["São Paulo", "Belo Horizonte", "Salvador", "Monte Belo", "Paranavaí"]
estado = ["SP", "MG","BA"]

#cidade_estado = zip_longest(indice, estado, cidade,fillvalue="estado")
cidade_estado = zip(indice, estado, cidade)

#for valor in cidade_estado:
    #(valor)

#desempacotamento
for indice, estado, cidade in cidade_estado:
    print(indice,estado,cidade)

