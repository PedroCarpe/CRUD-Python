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


print('\n1 - para cadastrar um usuário\n2 - para atualizar um cadastro\n3 - para deletar um cadastro')
operacao = input('Digite a operação desejada: ')

if operacao == '1':
    #print('\n___Cadastro__de__Cliente___')
    while True:
        dados_usuario = cadastrar()

        #Verifica se o usuario já foi cadastrado, com base no CPF
        mycursor.execute('SELECT cpf from pessoas')
        cpf_usuarios = mycursor.fetchall()

        for cpf_ in cpf_usuarios:
            #Retornar o registro, do qual tal CPF faz parte
            if cpf_[0] == dados_usuario[1][0]:

                print('\n'+'\u001b[31m'+'CPF já cadastrado!'+'\u001b[37m')
                mycursor.execute(f'SELECT * from pessoas WHERE cpf = "{cpf_[0]}"')
                usuario = mycursor.fetchall()
                mybd.commit()
                for usuarios in usuario:
                    print(usuarios)
                print('\n')
                dados = cadastrar()

        sql = 'INSERT INTO pessoas (nome,cpf,email,telefone) VALUES(%s,%s,%s,%s)'
        
        #variavel 'nome' escolhida aleatoriamente, como referencia
        for usuario in range(len(dados_usuario[0])):
            val = (dados_usuario[0][usuario],dados_usuario[1][usuario],dados_usuario[2][usuario],dados_usuario[3][usuario])
            mycursor.execute(sql,val)
            mybd.commit()

        resposta = input('\nQuer cadastrar outro cliente (sim/nao)? ')
        while resposta != 'sim' and resposta != 'nao':
            resposta = input('\nQuer cadastrar outro cliente (sim/nao)? ')
        if resposta == 'nao':
            break

elif operacao == '2':
    mycursor.execute('SELECT * FROM pessoas')
    myresult = mycursor.fetchall()

    print('')
    print('___Dados__Cadastrados___\n')
    for result in myresult:
        print(result)
    try:
        #print('\n___Atualização__de__Cadastro___')
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
        print('Erro, operação não efetuada!')

elif operacao == '3':
    #print('\n___Apagar__registro__de__usuário___')
    try:
        while True:
            cpf_usuario = deletar()
            sql = f"DELETE FROM pessoas WHERE cpf = {cpf_usuario}"        
            mycursor.execute(sql)
            mybd.commit()
            print(mycursor.rowcount," registro(s) apagado(s)!")
            
            resposta = input('\nQuer apagar outro cliente (sim/nao)? ')
            while resposta != 'sim' and resposta != 'nao':
                resposta = input('\nQuer apagar outro cliente (sim/nao)? ')
            if resposta == 'nao':
                break
    except:
        print('Erro encontrado')


#mycursor.close()
mybd.close()
