# o modo x cria o arquivo e permite adicionar
listaAlunos = ["Roberto","Lucas","Luan","Renata",
"Maria","Carlos","José","João","Raquel","Eduardo"];

db = open("projeto/alunos.txt","w",encoding="utf-8")

for aluno in listaAlunos:
    db.write(aluno+"\n")
    pass

db.close()

arquivo = open("projeto/alunos.txt","r+",encoding="utf-8")
#nome = arquivo.readline(10);
#nome = arquivo.readlines();
nome = arquivo.read();
print(nome)