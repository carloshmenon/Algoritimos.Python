#continuacao da aula 22-04

import mysql.connector

#criar conexao

def conectar():
    conexao =mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="atv22_04"
    )

    return conexao

def get_alunos():
    conexao= conectar()
    cursor= conexao.cursor()

    cursor.execute("select * from alunos")
    dados=cursor.fetchall()

    for aluno in dados:
        print(f"ID:{aluno[0]}| Nome: {aluno[1]} | Idade: {aluno[2]}")

    cursor.close()
    conexao.close()

#get_alunos()

def post_aluno():
    conexao=conectar()
    cursor=conexao.cursor()

    cursor.execute("insert into alunos(nome, idade) values (%s, %s)", (input("digite o nome do aluno: "), input ("digite a idade do aluno: ")))
    conexao.commit()

    print("aluno adicionado com sucesso! ")
    cursor.close()
    conexao.close()

#post_aluno()

def put_aluno():
    conexao=conectar()
    cursor=conexao.cursor()

    cursor.execute("update alunos set nome=%s, idade=%s where id=%s ", (input("digite o nome: "), int(input("digite a idade: ")), int(input("digite id: "))))
    conexao.commit()
    print("aluno alterado com sucesso")

    cursor.close()
    conexao.close()

#put_aluno()