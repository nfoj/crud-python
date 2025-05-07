#
import sqlite3 as comando

# create table

# table clientes
sql_clientes =
    '''
    CREATE TABLE IF NOT EXISTS Clientes (
        ID_Cliente INTERGER PRIMARY KEY AUTOINCREMENT,
        RG VARCHAR(12) NOT NULL,
        Nome_Cliente VARCHAR(30) NOT NULL,
        Sobrenome_Cliente VARCHAR(40) NOT NULL,
        Telefone VARCHAR(12),
        Rua VARCHAR(40),
        Numero VARCHAR(5),
        Bairro VARCHAR(25)
    );
    '''

# table produtos
sql_produtos =
    '''
    CREATE TABLE IF NOT EXISTS Produtos (
        ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome_Produto VARCHAR (30) NOT NULL,
        Tipo_Produto VARCHAR (25) NOT NULL,
        Preco DECIMAL (10,2) NOT NULL,
        Qtd_Estoque SMALLINT NOT NULL
    );
    '''

# table vendas
# Nota fiscal = SMALLINT or VARCHAR 
sql_vendas =
    '''
    CREATE TABLE IF NOT EXISTS Vendas (
        ID_Transacao INTEGER PRIMARY KEY AUTOINCREMENT,
        Nota_Fiscal SMALLINT NOT NULL,
        ID_Cliente INTEGER NOT NULL,
        Data_Compra DATETIME,
        ID_Produto INTEGER NOT NULL,
        Qtd_Vendas SMALLINT NOT NULL,
        FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
        FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID_Produto)  
    );
    '''

try:
    conexao = comando.connect('bancodedados.db')
    cursor = conexao.cursor()

    cursor.exexute(sql_clientes)
    cursor.execute(sql_produtos)
    cursor.execute(sql_vendas)

    conexao.commit()    

except comando.DatabaseError as erro:
    print("Erro no Banco de Dados", erro) # (f"Erro no banco de dados!: {erro}")

finally:
    if conexao:
        conexao.close()


# CREATE - Insert clientes
insere_cliente='''
    INSERT INTO Clientes (RG, Nome_Cliente, Sobrenome_Cliente, Telefone, Rua, Numero, Bairro)
    VALUES
    ('98765432109','Carlos','Silva','0081112222','Avenida Principal','123','Centro'),
    ('11223344556','Mariana','Oliveira','0083334444','Rua das Flores','789','Jardim'),
    ('66554433221','Pedro','Santos','0085556666','Travessa da Paz','101','Esperança');
'''


try:
    conexao = comando.connect('bancodedados.db')
    cursor = conexao.cursor()

    cursor.execute(insere_cliente)
    conexao.commit()

except comando.DatabaseError as erro:
    print("Erro do banco de dados!", erro)

else:
    resultado = cursor.execute("SELECT * FROM Clientes;")
    print(resultado.fetchall())

finally:
    if conexao:
        conexao.close()

## 


# Create - Insert Produtos
insere_produtos='''
    INSERT INTO Produtos (Nome_Produto, Tipo_Produto, Preco, Qtd_Estoque)
    VALUES
    ('Abacaxi', 'Fruta', 10.00, 4),
    ('Acabate', 'Fruta', 12.10, 5),
    ('Laranja', 'Fruta', 7.50, 20),
    ('Melancia', 'Frua', 20.20, 3);    
'''

try:
    conexao = comando.connect('bancodedados.db')
    cursor = conexao.cursor()

    cursor.execute(insere_produtos)
    conexao.commit()

except comando.DatabaseError as erro:
    print("Erro do banco de dados!", erro)

else:
    resultado = cursor.execute("SELECT * FROM Produtos")
    print(resultado.fetchall())

finally:
    if conexao:
        conexao.close()
## 


# CREATE - Insert Vendas
insere_vendas='''
    INSERT INTO vendas (Nota_Fiscala, ID_Cliente, Data_Compra, ID_Produto, Qtd_Vendas)
    VALUES
    (123, 1, '2025-03-12', 1, 2),
    (234, 2, '2025-03-12', 2, 2),
    (456, 3, '2025-03-12', 3, 10),
    (789, 4, '2025-03-12', 4, 3);
'''

try:
    conexao = commando.connect('bancodedados.db')
    cursor = conexao.cursor()

    cursor.execute(insere_vendas)
    conexao.commit()

except comando.DatabaseError as erro:
    print("Erro do banco de dados!", erro)

else:
    resultado = cursor.execute("SELECT * FROM Vendas")
    print(resultado.fetchall())

finally:
    if conexao:
        conaxao.close()
