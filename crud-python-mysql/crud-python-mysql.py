import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='db',
)

cursor = conexao.cursor()

# CREATE
# id =  
#nome_produto = "Abacaxi" # Abacate
#valor = 5 # 10

#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#cursor.commit()


# READ
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)


# Update
#nome_produto = "todynho"
#valor = 6
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()


# DELETE
#nome_produto = "todynho"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()


# cursor.execute(comando)
# conexao.commit()
# resultado = cursor.fetchall()
# print(resultado)


cursor.close()
conexao.close()
