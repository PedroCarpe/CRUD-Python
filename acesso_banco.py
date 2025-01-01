import os
import mysql.connector

from dotenv import load_dotenv
load_dotenv()

#Conexao com o banco de dados
def conecta_ao_banco():
    try:
        mybd = mysql.connector.connect(
        host = os.getenv('HOST'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'),
        database = os.getenv('DATABASE')
        )
        conexao = mybd.cursor()
        return conexao,mybd
    except:
        print('Erro ao conectar ao Banco de Dados!!')
