import mysql.connector
import mysql.connector as sql

try:
    #Cria conexão ao banco de dados
    con = mysql.connector.Connect(host='localhost', database='cadastro', user='root', password='')

    #Declaração SQL a ser executada
    criar_tabela_SQL = """CREATE TABLE familiares(
                            id_familiar int not null,
                            tipo_familiar varchar(20),
                            nome_familiar varchar(20) not null,
                            id_gafanhoto int not null,
                            foreign key(id_gafanhoto) references gafanhotos(id),
                            primary key(id_familiar)
                            );
    
    """

    #Cria cursos e executa SQL no banco de dados
    cursor = con.cursor()     #cursos permite fazer alteração por elementos de uma tabela retornados
    cursor.execute(criar_tabela_SQL)
    linha = cursor.fetchone()
    print("Tabela de familiares criada com sucesso!!!")

except mysql.connector.Error  as error:
    print(f"Falha ao tentar criar a tabela no Mysql: {error}")
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("A conexão com o Mysql foi encerrada")