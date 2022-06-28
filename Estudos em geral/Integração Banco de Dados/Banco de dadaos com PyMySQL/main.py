import pymysql.cursors

# Abrir uma conexão a um banco de dados

con = pymysql.connect(host='localhost', user='root', database='cadastro', password='', cursorclass=pymysql.cursors.DictCursor)

#Preparara  um cursor com o método .cursor()
with con.cursor() as c:

    #Cria uma consulta
    sql = 'select nome from gafanhotos'
    c.execute(sql)
    res = c.fetchall()
    print(res)
    print()
    #Vantagens de usar Dicionário
    #print("Livro Retornado: ", res['Nome da coluna que deseja filtrar '])

    #outra consultar
    sql = 'select * from cursos'
    c.execute(sql)
    res = c.fetchall()
    print(res)
    print()
    for linha in res:
        print(linha['Cursonome'])
    con.close()