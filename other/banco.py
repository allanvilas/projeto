# -Instrução que importa os comandos
# -do banco de dados.
import sqlite3

# Comando que conecta ao banco de dados.
conection = sqlite3.connect('database/projeto.sqlite3')

# -Objeto que navega no banco de dados.
cursor = conection.cursor()

# -Comando SQL que queromos executar no banco de dados.
comandoSQL = 'SELECT aluno_nome FROM aluno;'

# -Comando que executa as instruções nos dados.
resultado = cursor.execute(comandoSQL)

resultado = resultado.fetchall()

#Resultado da consulta
for objeto in resultado:
    print(" NOME: "+objeto[0])
    pass
