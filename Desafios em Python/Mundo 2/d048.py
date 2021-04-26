#soma impares multiplos de 3 de 1 a 500

soma=0
cont=0
for i in range(1,501,2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
        
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
