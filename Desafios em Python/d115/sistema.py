from lib.interface import *
from lib.arquivo import *
from time import  sleep

arq = 'cursoemvideos.txt'

if arquivoExiste(arq):
    print("arquivo encontrado com sucesso")
else:
    print("arquivo não encontrado")
    criarArquivo(arq)
while True:
    resposta  = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa' , 'Sair do Sistema'])
    if  resposta == 1:
        #opção de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("Opção 2")
    elif resposta == 3:
        cabeçalho("Saindo do sistema, até logo!")
        break
    else:
        print("\033[31mERRO!, digite uma opção valida! \033[m")
    sleep(2)



