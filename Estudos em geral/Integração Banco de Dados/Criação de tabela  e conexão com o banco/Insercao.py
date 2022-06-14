import mysql.connector
from mysql.connector import Error

try:
    # Cria conexão ao banco de dados
    con = mysql.connector.Connect(host='localhost', database='cadastro', user='root', password='')

    # Declaração SQL a ser executada
    inserir_familiar = """insert into familiares values
                            ('1', 'irmão', 'Josefo', '2'), 
                            ('2', 'Pai', 'Joel', '1');

    """
    # Cria cursos e executa SQL no banco de dados
    cursor = con.cursor()
    cursor.execute(inserir_familiar)
    con.commit()
    print("Registro inserido na tabela !!!")

except Error as error:
    print(f"Falha ao inserir dados no Mysql: {error}")
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
