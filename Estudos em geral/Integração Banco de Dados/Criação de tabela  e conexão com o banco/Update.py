import mysql.connector
from mysql.connector import Error

#Atualizar registros em um banco de dados Mysql

def conectar():
    try:
        global con
        con = mysql.connector.Connect(host='localhost', database='cadastro', user='root', password='')
    except Error as erro:
        print("Erro de conexão", erro)

def consulta(idFamiliar):
    try:
        conectar()
        consulta_sql = f'select * from familiares where id_familiar = {idFamiliar}'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print("\nID >", linha[0])
            print("Tipo Familiar >", linha[1])
            print("Nome >", linha[2])
            print("ID Gafanhoto >", linha[3], "\n")

    except Error as erro:
        print(f"Falha ao consultar tabela: {erro}")
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()


def atualiza(declaracao):
    try:
        conectar()
        altera_nome = declaracao
        cursor = con.cursor()
        cursor.execute(altera_nome)
        con.commit()
        print("Nome alterado com sucesso")
    except Error as erro:
        print(f"Falha ao inserir dados na tabela: {erro}")
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()


if __name__ == '__main__':  #indica onde o programa irá iniciar
    print("Atualizar nome dos familiares no banco de dados")
    print("Entre com os dodos conform solicitado")

    print("\nInforme o códico do familar a alterar")
    idFamiliar = input("ID Familiar > ")

    consulta(idFamiliar)

    print("\nEntre com o novo nome do Familiar")
    nome_fami =  input("Novo Nome:")

    declaracao = f"""UPDATE familiares
    set nome_familiar = '{nome_fami}'
    where id_familiar  = '{idFamiliar}'
    
    """

    #EXECUTAR O UPDATE NO BANCO
    #print(declaracao)
    atualiza(declaracao)

    verifica = input("Deseja consultar a atualização? s = sim, n = não: ")

    if (verifica == 's'):
        consulta(idFamiliar)
    else:
        print("Programa Finalizado")