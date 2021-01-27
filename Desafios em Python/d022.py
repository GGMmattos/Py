#Analisador de Textos

nome=str(input('Informe seu nome: ')).strip()

print('\nMaiusculas: {}'.format(nome.upper()))

print('Minusculas: {}'.format(nome.lower()))

print('Seu nome tem ao todos {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
