import os
turmas = []
notas = []


controle = True


def menu():
    print("====================")
    print("       Escola       ")
    print("====================")
    print("     -= Menu =-     ")
    print("Opções:")
    print("1 - Cadastrar Turmas/Aluno")
    print("2 - Exibir turma    ")
    print("3 - Cadastrar nota  ")
    print("4 - Exibir nota  ")
    print("0 - Sair")
    print("====================")
    pass

def cadastrarTurmas(qtd):
    nomeTurma = input("Digite o codigo da turma\n:: ")
    try:
        arquivoTurma = open("turmas/"+nomeTurma+".txt","x",encoding="utf-8")
    except FileExistsError:
        print("     !!ERRO!! \n Esse codigo de turma ja é utilizado \n Tente novamente.")
        input("\nDigite para continuar...\n")
        cadastrarTurmas(qtd)
        pass
    except FileNotFoundError:
        print("Criando arquivo...")
        arquivoTurma = open("turmas/"+nomeTurma+".txt","x",encoding="utf-8")
        input("\nArquivo criado com sucesso! \nDigite para continuar...\n")
        pass
    except OSError:
        input("\nErro do windows\n Digite para continuar... \n")
        cadastrarTurmas(qtd)
        pass
    numero = 1
    for aluno in range(qtd):
        nomeAluno = input("Insira o nome do aluno:\n")
        turmas.append([nomeAluno,numero])
        #aumenta a contagem de alunos
        arquivoTurma.write(nomeAluno+"\n")
        numero += 1
        pass

    print("Lista dos alunos:\n")
    print(turmas)
    input("Digite para continuar...")

    arquivoTurma.close()
    pass

def visualizarTurma(turma):
    print("====================")
    print("       Turma        ")
    print("====================")
    print("|Nº |Nome:          ")
    for aluno in range(len(turma)):
        print("|",turma[aluno][1],"| ",turma[aluno][0])
        pass
    input("Digite para continuar...")
    pass

def cadastrarNotas(alunos):

    for id in range(len(alunos)):
        nomeAluno = alunos[id][0]
        idAluno = alunos[id][1]
        print("====================")
        print("   Cadastrar Nota   ")
        print("Aluno: ",nomeAluno)
        print("====================")
        nota = [0,0,0]
        nota[0] = idAluno
        nota[1] = int(input("Insira a primeira nota \nN1: "))
        nota[2] = int(input("Insira a segunda nota  \nN2: "))

        notas.append(nota)
        pass
    pass

def exibirNotas(notas):
    print(" ======================= ")
    print("| N1  N2  - Nome Aluno|")
    for nota in range(len(notas)):
        print("| ",notas[nota][1]," ",notas[nota][2],"  ", turmas[nota][0])
        pass
    input("Digite para continuar...")
    pass

while controle == True:
    menu()
    #VARIÁVEL OPÇÃO RECEBE A OPÇÃO QUE O USUÁRIO SELECIONA NO SISTEMA
    opcao = int(input("Insira a opção:\n"))

    match (opcao):
        #O CASE 0 EXECUTA A SAIDA DO SISTEMA
        case(0):
            print("Saindo...")
            controle = False
        case(1):
            print(".* Criando Turma *.")
            qtdNovaTurma = int(input("Insira a quantidade:\n"))
            cadastrarTurmas(qtdNovaTurma)
        case(2):
            visualizarTurma(turmas)
        case(3):
            cadastrarNotas(turmas)
        case(4):
            exibirNotas(notas)
        case(5):
            print(os.listdir("."))
    pass

print("fim da execução")