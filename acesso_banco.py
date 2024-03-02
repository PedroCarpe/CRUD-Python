import mysql.connector

#Conexao com o banco de dados
def conecta_ao_banco():
    try:
        mybd = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'senha',
        database = 'usuarios'
        )
        conexao = mybd.cursor()
        return conexao,mybd
    except:
        print('Erro ao conectar ao Banco de Dados!')