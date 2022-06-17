import mysql.connector
from mysql.connector import Error



escolha = input("Deseja inserir um registro 0/1:")

while escolha == "1":

    print("\nEntre com os dados conforme solicitado")

    tipo_familiar = input("Parentesco: ")
    nome_familiar = input("Nome: ")
    id_gafanhoto = input("ID gafanhoto: ")
    

    dados = tipo_familiar +'\'' + ',\'' + nome_familiar +'\','+'\''+ id_gafanhoto + '\'' ')'
    declaracao = """insert into familiares values
                    ('default', '"""
    sql = declaracao + dados
    print(sql)
    try:
        #Cria conexão ao banco de dados
        con = mysql.connector.Connect(host='localhost', database='cadastro', user='root', password='')

        #Declaração SQL a ser executada
        inserir_familiar = sql
        # Cria cursos e executa SQL no banco de dados
        cursor = con.cursor()
        cursor.execute(inserir_familiar)
        con.commit()
        print(cursor.rowcount, "Registro inserido na tabela !!!")
        escolha = input("Deseja inserir outro registro ? 0/1:")


    except Error as error:
        print(f"Falha ao inserir dados no Mysql: {error}")
    finally:

        if (con.is_connected()):
            cursor.close()
            con.close()

print("Programa finalizado")