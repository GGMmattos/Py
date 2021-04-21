from lib.interface import *
from time import  sleep

while True:
    resposta  = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa' , 'Sair do Sistema'])
    if  resposta == 1:
        cabeçalho("Opção 1")
    elif resposta == 2:
        cabeçalho("Opção 2")
    elif resposta == 3:
        cabeçalho("Saindo do sistema, até logo!")
        break
    else:
        print("\033[31mERRO!, digite uma opção valida! \033[m")
    sleep(2)



