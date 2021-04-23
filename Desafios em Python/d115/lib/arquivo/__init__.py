from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')   #abertura de arquivos, neste caso para leitura
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a =  open(nome, 'wt+') #Escreve um arquivo de texto, caso o mesmo n exita cria(oq simboliza o +)
        a.close()
    except:
        print("Houve um erro na crianção doa arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")

def lerArquivo(nome):
    try:
        a =  open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        print(a.readLines())

