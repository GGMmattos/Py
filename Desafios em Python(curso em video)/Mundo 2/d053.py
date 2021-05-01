#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input("Dgite um frase: ")).strip().upper()

palavra = frase.split()
junto = ''.join(palavra)

inverso = ''
inverso = junto[::-1] # simplificado

'''for i in range(len(junto)-1,-1,-1): #com laço FOR
    inverso+= junto[i]'''

print('Inverso de {} é {}'.format(junto,inverso))

if inverso == junto:
    print('\nA frase é um PALÍNDROMO')
else:
    print("\nA frase NÃO É PALÍNDROMO")
