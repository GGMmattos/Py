import mysql.connector
import mysql.connector as sql
con = mysql.connector.Connect(host='localhost', database='cadastro', user='root', password='')

if con.is_connected():
    db_info = con.get_server_info()
    print(f"Conectado ao servidor Mysql versão{db_info}")
    cursor = con.cursor()     #cursos pewrmite fazer alteração por elementos de uma tabela retornados
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print(f"Conectado ao banco de dados{linha}")

if con.is_connected():
    cursor.close()
    con.close()
    print("A conexão com o Mysql foi encerrada")