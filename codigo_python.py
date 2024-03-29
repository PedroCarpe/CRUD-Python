#A ideia do algoritmo, é simular o cadastro de um cliente/usuario 
#APF, verificar valores duplicados quando for inserir, tratamento de erro

def criar_nome():
    nome = []

    nome_ = input('Digite seu nome: ')
    copia_nome = nome_
    nome_ = nome_.split()
    
    for partes_nome in nome_:
        if partes_nome.isalpha() == True:
            boleana = True
        else:
            boleana = False
            break

    if boleana == True:
        nome.append(copia_nome)
    else:
        print('\u001b[31m'+'Nome incorreto, digite novamente!'+'\u001b[37m')
        temp = criar_nome()
        temp = temp[0]
        nome.append(temp) 
    
    return nome


def criar_cpf():
    cpf = []

    cpf_ = input('Digite seu CPF(somente números/sem espaços): ')

    if cpf_.isnumeric() == True:
        boleana = True
    else:
        boleana = False
    
    if boleana == True:
        cpf.append(cpf_)   
    else:
        print('\u001b[31m'+'CPF incorreto, digite novamente!'+'\u001b[37m')
        temp = criar_cpf()
        temp = temp[0]
        cpf.append(temp)      

    return cpf


def criar_email():
    email = []

    email_ = input('Digite seu email: ')

    if email_.find('@') != -1:
        boleana = True
    else:
        boleana = False

    if boleana == True:
        email.append(email_)
    else:
        print('\u001b[31m'+'Email incorreto, digite novamente!'+'\u001b[37m')
        temp = criar_email()
        temp = temp[0]
        email.append(temp)    
    
    return email


def criar_telefone():
    telefone = []

    telefone_ = input('Digite seu Telefone(somente números/sem espaços): ')

    if telefone_.isnumeric() == True:
        boleana = True
    else:
        boleana = False

    if boleana == True:
        telefone.append(telefone_)
    else:
        print('\u001b[31m'+'Telefone incorreto, digite novamente!'+'\u001b[37m')
        temp = criar_telefone()
        temp = temp[0]
        telefone.append(temp)
 
    return telefone


def cadastrar():
    print('\n___Cadastro__de__Cliente___')
    nome = criar_nome()
    cpf = criar_cpf()
    email = criar_email()
    telefone = criar_telefone()

    return nome,cpf,email,telefone                
            

def atualizar():
    print('\n___Atualização__de__Cadastro___')
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
    print('\n___Apagar__registro__de__usuário___')
    cpf_usuario = input('Digite o CPF do usuário que deseja apagar: ')
    return cpf_usuario

  