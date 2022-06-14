import mysql.connector
from mysql.connector import Error

try:
    #Cria conexão ao banco de dados
    con = mysql.connector.Connect(host='localhost', database='cadastro', user='root', password='')

    consulta_sql = "select * from familiares"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número de registros retornados: ", cursor.rowcount)

    print("Monstrando gafanhotos cadastrados")
    for linha in linhas:
        print("ID:", linha[0])
        print("Tipo Familiar:", linha[1])
        print("Nome familiar:", linha[2])
        print("ID do gafanhoto:", linha[3], "\n")

except Error as e:
    print("Erro ao acessar a tabela", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao Mysql encerrada")
