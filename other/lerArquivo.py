arquivo = open("projeto/alunos.txt",'r',encoding="utf-8")

alunos = [];

for aluno in arquivo:
    alunos.append(aluno[:-1]);
    pass

print(alunos)
