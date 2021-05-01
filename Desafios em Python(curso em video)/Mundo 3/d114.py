#Crie um código em Python que teste se um site fornecido pelo usuário está acessivel no momento

import urllib
import urllib.request

site = str(input('Digite o link do site: \033[36m'))

try:
    site1 = urllib.request.urlopen('https://www.' + site + '/')
except urllib.request.URLError:
    print('\n\033[31m Este Site, Não Está Acessível No Momento. \033[m')
else:
    print('\n\033[32m Este Site, Está Ativo ! \033[m')