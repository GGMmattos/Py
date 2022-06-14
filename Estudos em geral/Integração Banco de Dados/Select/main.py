import mysql.connector
from mysql.connector import Error

try:
    #Cria conexão ao banco de dados
    con = mysql.connector.Connect(host='localhost', database='cadastro', user='root', password='')

    consulta_sql = "select * from gafanhotos"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número de registros retornados: ", cursor.rowcount)

    print("Monstrando gafanhotos cadastrados")
    for linha in linhas:
        print("ID:", linha[0])
        print("Nome:", linha[1])
        print("Profissão:", linha[2])
        print("Nascimento:", linha[3])
        print("Sexo:", linha[4])
        print("Peso:", linha[5])
        print("Altura:", linha[6])
        print("Nascionalidade:", linha[7])
        if (linha[8] is None):
            print("Sem curso preferido\n")
        else:
            print("Curso preferido: ", linha[8], "\n")

except Error as e:
    print("Erro ao acessar a tabela", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao Mysql encerrada")
