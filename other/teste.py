arquivo = 0

try:
    arquivo = open("alunos.txt","r",encoding = "utf-8")
    print("O arquvio existe e foi aberto!")
except FileNotFoundError:
    print("O arquivo não existe!")
finally:
    print("Tentando criar o arquivo!")
    try:
        arquivo = open("alunos.txt","w",encoding = "utf-8")
        print("Arquivo criado com sucesso!")
        pass
    except:
        print("O arquivo não pode ser criado!")
        pass

arquivo.write("Gustavo\n")
arquivo.write("Maria\n")
arquivo.write("Jonas\n")
arquivo.write("Pedro\n")

