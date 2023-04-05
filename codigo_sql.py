#A ideia do algoritmo, é simular o cadastro de um cliente/usuario
import mysql.connector
from codigo_python import cadastrar,atualizar,deletar


#Conexao com o banco de dados
mybd = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'senha',
database = 'usuarios'
)
mycursor = mybd.cursor()

print('4 - para deletar um registro')
operacao = input('Digite a operação desejada: ')

'''print('___Cadastro__de__Cliente___')
while True:
    dados_usuario = cadastrar()

    sql = ('INSERT INTO pessoas (nome,cpf,email,telefone) VALUES(%s,%s,%s,%s)')

    for usuario in range(len(dados_usuario[0])):
        val = (dados_usuario[0][usuario],dados_usuario[1][usuario],dados_usuario[2][usuario],dados_usuario[3][usuario])
        mycursor.execute(sql,val)
        mybd.commit()

    resposta = input('\nQuer cadastrar outro cliente (sim/nao)? ')
    if resposta == 'nao':
        break'''

if operacao == '4':
    print('\n___Apagar__registro__de__usuário___')
    while True:
        cpf_usuario = deletar()
        sql = f"DELETE FROM pessoas WHERE cpf = {cpf_usuario}"        
        mycursor.execute(sql)
        mybd.commit()
        print(mycursor.rowcount," registro(s) afetado(s)!")
        resposta = input('\nQuer apagar outro cliente (sim/nao)? ')

        if resposta != 'sim':
            break

'''resposta_atualizar = input('\nQuer atualizar seus dados (sim/nao)? ')
if resposta_atualizar == 'sim':
    mycursor.execute('SELECT * FROM pessoas')
    myresult = mycursor.fetchall()

    print('')
    print('___Dados__Cadastrados___\n')
    for result in myresult:
        print(result)
    try:
        print('\n___Atualização__de__Cadastro___')
        dados_ = atualizar()
        sql = f"UPDATE pessoas SET {dados_[2]} = '{dados_[0]}' WHERE {dados_[2]} = '{dados_[1]}'"
        mycursor.execute(sql)
        mybd.commit()
        print(mycursor.rowcount," registro(s) afetado(s)!")
        
        mycursor.execute(f"SELECT * FROM pessoas WHERE {dados_[2]} = '{dados_[0]}'")
        myresult = mycursor.fetchall()

        print('')
        print('___Registro(s)__Cadastrado(s)___\n')
        for result in myresult:
            print(result)
    except:
        print('Erro, operação não efetuada!')'''   

#--------------------------------------------------------------------------------
'''sql = ('INSERT INTO pessoas (nome,cpf,email,telefone) VALUES(%s,%s,%s,%s)')

#variavel 'nome' escolhida aleatoriamente, como referencia
for usuario in range(len(nome)):
    val = (nome[usuario],cpf[usuario],email[usuario],telefone[usuario])
    mycursor.execute(sql,val)
    mybd.commit()'''

#---------------------------------------------------------------------------------
'''mycursor.execute('SELECT * FROM pessoas')
myresult = mycursor.fetchall()

print('')
print('___Dados__Cadastrados___\n')
for result in myresult:
    print(result)'''

mycursor.close()
mybd.close()