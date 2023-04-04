# Criar um programa, que tenha um menu, e nesse menu tenha as seguintes opções

# 1- Cadastrar um usuario (Nome, Telefone, idade, profissão)
# 2- Listar os usuarios cadastrados
# 3- Remover um usuário
# 0- Sair


listaUsuarios = []

opcao = 0


def printaMenu():
    print("****************************")
    print("*  1 - Cadastrar Usuário   *")
    print("*  2 - Listar Usuário      *")
    print("*  3 - Remover Usuário     *")
    print("*  0 - Sair                *")
    print("****************************")


def cadastrarUsuario(nome, telefone, profissao, idade):
    lista = []
    lista.append(nome)
    lista.append(telefone)
    lista.append(profissao)
    lista.append(idade)
    listaUsuarios.append(lista)


def listar(lista):
    if len(lista) == 0:
        print("*****************************")
        print("* Lista de usuários vazios! *")
        print("*****************************")

    for i in lista:
        print(i)

# [
#
# [0]      [[0]Otni, [1]999, [2]profissao, [3]25],
# [1]      [[0]Juaquina, [1]999, [2]profissao, 25]
#
# ]


def removeUsuario(nome):
    for i in listaUsuarios:
        for x in i:
            if (x == nome):
                listaUsuarios.remove(i)
                print("*********************************")
                print("* Usuário removido com sucesso! *")
                print("*********************************")

                break
            else:
                print("*************************************")
                print("* Esse usuário não está cadastrado! *")
                print("*************************************")
                break


def metodoDeInicio():


    printaMenu()
    opcao = int(input("Digite uma opção: "))


    while (True):

        if opcao == 1:
            nome = input("Digite um nome: ")
            telefone = input("Digite um telefone: ")
            profissao = input("Digite um profissao: ")
            idade = input("Digite um idade: ")
            cadastrarUsuario(nome, telefone, profissao, idade)

            printaMenu()
            opcao = int(input("Digite uma opção: "))

        elif opcao == 2:
            listar(listaUsuarios)
            printaMenu()
            opcao = int(input("Digite uma opção: "))

        elif opcao == 3:
            nome = input("Digite o nome do usuário que deseja remover: ")
            removeUsuario(nome)
            printaMenu()
            opcao = int(input("Digite uma opção: "))

        elif opcao == 0:
            print("*******************************")
            print("* Encerrando os trabalhos ... *")
            print("*******************************")
            break

        else:
            print("********************")
            print("* Opção invalida!! *")
            print("********************")
            printaMenu()
            opcao = int(input("Digite uma opção: "))


metodoDeInicio()