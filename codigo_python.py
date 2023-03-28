#A ideia do algoritmo, é simular o cadastro de um cliente/usuario
#APF, validar entradas dos campos, 
#APF, eliminar as 'listas globais', por listas internas as funções

nome = []
cpf = []
email = []
telefone = []

    
def criar_nome():
    global nome
    
    nome_ = input('Digite seu nome: ')
    copia_nome = nome_
    nome_ = nome_.split()
    
    for partes_nome in nome_:
        if partes_nome.isalpha() == True:
            boleana = True
        else:
            boleana = False
            break

    print(boleana)
    if boleana == True:
        #print('\u2705')
        nome.append(copia_nome)
        #return nome
    else:
        print('\u001b[31m'+'Nome incorreto, digite novamente!'+'\u001b[37m')
        criar_nome()      
    
    return nome

def criar_cpf():
    global cpf

    cpf_ = input('Digite seu CPF(somente números/sem espaços): ')

    if cpf_.isnumeric() == True:
        boleana = True
    else:
        boleana = False

    
    if boleana == True:
        cpf.append(cpf_)
        #return cpf
    else:
        print('\u001b[31m'+'CPF incorreto, digite novamente!'+'\u001b[37m')
        criar_cpf()      

    return cpf

def criar_email():
    global email

    email_ = input('Digite seu email: ')

    if email_.find('@') != -1:
        boleana = True
    else:
        boleana = False

    
    if boleana == True:
        email.append(email_)
        #return email
    else:
        print('\u001b[31m'+'Email incorreto, digite novamente!'+'\u001b[37m')
        criar_email()    
    
    return email

def criar_telefone():
    global telefone

    telefone_ = input('Digite seu Telefone(somente números/sem espaços): ')

    if telefone_.isnumeric() == True:
        boleana = True
    else:
        boleana = False


    if boleana == True:
        telefone.append(telefone_)
        #return telefone
    else:
        print('\u001b[31m'+'Telefone incorreto, digite novamente!'+'\u001b[37m')
        criar_telefone()    
 
    return telefone

#será se os nomes dessas listas se confundem, com os nomes das listas 'globais'?
def cadastrar():
    nome = criar_nome()
    cpf = criar_cpf()
    email = criar_email()
    telefone = criar_telefone()

    return nome,cpf,email,telefone                
            

def atualizar():
    print('Opções de atualização:\n1 - Nome;\n2 - CPF;\n3 - Email;\n4 - Telefone;\n')
    opcao = input('Digite a opção desejada: ')
    
    if opcao == '1':
        antigo_nome = input('Digite o antigo nome: ')
        novo_nome = input('Digite o novo nome: ')
        dados_ = novo_nome,antigo_nome,'nome'
    elif opcao == '2':
        antigo_cpf = input('Digite o antigo CPF: ')
        novo_cpf = input('Digite o novo CPF: ')
        dados_ = novo_cpf,antigo_cpf,'cpf'
    elif opcao == '3':
        antigo_email = input('Digite o antigo email: ')
        novo_email = input('Digite o novo email: ')
        dados_ = novo_email,antigo_email,'email'
    elif opcao == '4':
        antigo_tel = input('Digite o antigo telefone: ')
        novo_tel = input('Digite o novo telefone: ')
        dados_ = novo_tel,antigo_tel,'telefone'

    return dados_

def deletar():
    pos = nome.index(input('Digite o nome que deseja apagar: '))
    #id1.pop(pos)
    cpf.pop(pos)
    email.pop(pos)
    telefone.pop(pos)
    nome.pop(pos)


#vetor = [id1[0],nome[0],cpf[0],email[0],telefone[0]]

'''resposta=input('\nDeseja apagar um cadastro (sim/nao)? ')
if resposta=='sim':
    try:
        print('___Apagar__Cadastro___')
        Deletar()
    except:
        print('Cliente não encontrado!')'''
    
#for t in range(len(id1)):
#    print('\n___Dados__Cadastrados___\n'+'Nome: '+nome[t]+'\n'+'CPF: '+cpf[t][0:3]+'.'+cpf[t][3:6]+'.'+cpf[t][6:9]+'-'+cpf[t][9:]+'\n'+'Email: '+email[t]+'\n'+'Telefone: ('+telefone[t][0:2]+') '+telefone[t][2:])    
  