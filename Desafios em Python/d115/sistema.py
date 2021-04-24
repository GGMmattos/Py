from lib.interface import *
from lib.arquivo import *
from time import  sleep

arq = 'cursoemvideos.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa' , 'Sair do Sistema'])
    if  resposta == 1:
        #opção de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho("Opção 2")
    elif resposta == 3:
        cabecalho("Saindo do sistema, até logo!")
        break
    else:
        print("\033[31mERRO!, digite uma opção valida! \033[m")
    sleep(2)



