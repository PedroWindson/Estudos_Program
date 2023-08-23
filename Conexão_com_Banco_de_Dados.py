import mysql.connector
from mysql.connector import Error
opt = 0

try:
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='teste_pdo')
except Error as erro:
        print(erro)

while(opt != 5):
    option = 1
    print('------------------------------------')
    print('----------CRUD DE USUARIOS----------')
    print('------------------------------------')
    print('\n1 - Inserir dados')
    print('2 - Consulta')
    print('3 - Atualizar registro')
    print('4 - Deletar registro')
    print('5 - Parar execução')

    opt = int(input('\nDigite a opção: '))

    if(opt == 1):
        while (option == 1):
            nome = input("Digite nome do usuario: ")
            email = input("Digite email: ")

            try:
                inserir_dados = "INSERT INTO usuarios values(0, '{}', '{}')".format(nome, email)
                cursor = cnx.cursor()
                cursor.execute(inserir_dados)
                cnx.commit()
                print('Registro inserido!')
                input('\nEnter para continuar...')

            except Error as erro:
                print(erro)

            print("------------------------------------")
            print("1 - Continuar Inserindo dados")
            print("2 - Voltar para menu principal")
            option = int(input("\nSua opção: "))

            while (option != 1 and option != 2):
                print('número inválido!')
                print("------------------------------------")
                print("1 - Continuar Inserindo dados")
                print("2 - Voltar para menu principal")
                option = int(input("\nSua opção: "))

    elif(opt == 2):
        while(option == 1):
            varid = (input('Digite ID para consulta: '))

            try:
                consulta = "SELECT * FROM usuarios WHERE id={};".format(varid)
                cursor = cnx.cursor()
                cursor.execute(consulta)
                linha = cursor.fetchone()

                print('\nId: {}'.format(linha[0]))
                print('Nome: {}'.format(linha[1]))
                print('E-mail: {}'.format(linha[2]))
                input('\nEnter para continuar...')

            except Error as erro:
                print(erro)

            print("------------------------------------")
            print("1 - Continuar consultando dados")
            print("2 - Voltar para menu principal")
            option = int(input("\nSua opção: "))

            while (option != 1 and option != 2):
                print('número inválido!')
                print("------------------------------------")
                print("1 - Continuar consultando dados")
                print("2 - Voltar para menu principal")
                option = int(input("\nSua opção: "))

    elif(opt == 3):

        while (option == 1):
            escolha = 0
            alterar = 0 # 1 - para alterar dados da consulta; 2 - Para não alterar dados;
            varid = input('Digite o ID que deseja atualizar: ')

            try:
                consulta = "SELECT * FROM usuarios WHERE id={};".format(varid)
                cursor = cnx.cursor()
                cursor.execute(consulta)
                linha = cursor.fetchone()

                print('\nId: {}'.format(linha[0]))
                print('Nome: {}'.format(linha[1]))
                print('E-mail: {}'.format(linha[2]))
                input('\nEnter para continuar...')

            except Error as erro:
                print(erro)

            print("\nDeseja alterar os dados?")
            print("1 - Sim")
            print("2 - Não")

            alterar = int(input("\nDigite a opção: "))

            if(alterar == 1):
                print("\nQual campo deseja atualizar?")
                print("1 - Atualizar Apenas Nome")
                print("2 - Atualizar Apenas E-mail")
                print("3 - Atualizar Nome e E-mail")

                escolha = int(input('Sua Escolha: '))

                if (escolha == 1):
                    nome = input("Digite o nome: ")
                    try:
                        update = "UPDATE usuarios SET nome='{}' WHERE id={};".format(nome, varid)
                        cursor = cnx.cursor()
                        cursor.execute(update)
                        cnx.commit()

                        print('Registro atualizado!')
                        input('\nEnter para continuar...')

                    except Error as erro:
                        print(erro)

                elif (escolha == 2):
                    email = input("Digite o email: ")
                    try:
                        update = "UPDATE usuarios SET email='{}' WHERE id={};".format(email, varid)
                        cursor = cnx.cursor()
                        cursor.execute(update)
                        cnx.commit()

                        print('Registro atualizado!')
                        input('\nEnter para continuar...')

                    except Error as erro:
                        print(erro)

                elif (escolha == 3):
                    nome = input("Digite o nome: ")
                    email = input("Digite o nome: ")
                    try:
                        update = "UPDATE usuarios SET nome='{}', email='{}' WHERE id={};".format(nome, email, varid)
                        cursor = cnx.cursor()
                        cursor.execute(update)
                        cnx.commit()

                        print('Registro atualizado!')
                        input('\nEnter para continuar...')

                    except Error as erro:
                        print(erro)
            elif(alterar == 2):
                print('')


            print("------------------------------------")
            print("1 - Continuar atualizando dados")
            print("2 - Voltar para menu principal")
            option = int(input("\nSua opção: "))

            while (option != 1 and option != 2):
                print('número inválido!')
                print("------------------------------------")
                print("1 - Continuar atualizando dados")
                print("2 - Voltar para menu principal")
                option = int(input("\nSua opção: "))

    elif(opt == 4):
        while (option == 1):
            excluir = 0  # 1 - para excluir registro; 2 - Para não excluir registro;
            varid = (input('Digite ID: '))

            try:
                consulta = "SELECT * FROM usuarios WHERE id={};".format(varid)
                cursor = cnx.cursor()
                cursor.execute(consulta)
                linha = cursor.fetchone()

                print('\nId: {}'.format(linha[0]))
                print('Nome: {}'.format(linha[1]))
                print('E-mail: {}'.format(linha[2]))
                input('Enter para continuar...')

            except Error as erro:
                print(erro)

            print("\nDeseja excluir esse registro?")
            print("1 - Sim")
            print("2 - Não")

            excluir = int(input("\nDigite a opção: "))

            if(excluir == 1):
                try:
                    delete = "DELETE FROM usuarios WHERE id={}".format(varid)
                    cursor = cnx.cursor()
                    cursor.execute(delete)
                    cnx.commit()

                    print('Registro excluido!')
                    input('\nEnter para continuar...')

                except Error as erro:
                    print(erro)
            elif(excluir == 2):
                print('')


            print("------------------------------------")
            print("1 - Continuar excluindo dados")
            print("2 - Voltar para menu principal")
            option = int(input("\nSua opção: "))

            while (option != 1 and option != 2):
                print('número inválido!')
                print("------------------------------------")
                print("1 - Continuar excluindo dados")
                print("2 - Voltar para menu principal")
                option = int(input("\nSua opção: "))

    elif(opt > 5 and opt < 1):
        print('número inválido')
        opt = 0




cnx.close()