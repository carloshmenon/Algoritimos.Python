#continuacao da aula 22-04
#continuacao aula 30-04
import mysql.connector

from db import conectar
#transformar em api flask

from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route("/alunos", methods = ["GET"])

def get_alunos():
    conexao= conectar()
    cursor= conexao.cursor()

    cursor.execute("select * from alunos")
    dados=cursor.fetchall()

    alunos=[] #aqui abrimos uma lista para realizar um append
    for aluno in dados:
        alunos.append({
                "id": aluno[0],
                "nome": aluno[1],
                "idade": aluno [2]
        })
    
    cursor.close()
    conexao.close()

    return jsonify(alunos)

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

if __name__ == "__main__":
    app.run(debug=True)

