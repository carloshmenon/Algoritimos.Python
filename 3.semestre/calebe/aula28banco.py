import mysql.connector 
from db import conectar
#transformar em api flask
from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("select * from alunos")
    alunos = cursor.fetchall()

   # alunos = []
   # for aluno in dados:
    #    alunos.append({
     #           "id": aluno[0],
      #          "nome": aluno[1],
       #         "idade": aluno[2]
        #    })
        #print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}")
    
    cursor.close()
    conexao.close()

    return render_template ("aula.html", alunos=alunos)

#get_alunos()

def post_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("insert into alunos(nome, idade) values (%s, %s)", (input("Digite o nome do aluno: "), input("Digite a idade do aluno: ")))
    conexao.commit()

    print("Aluno adicionado com sucesso!")
    cursor.close()
    conexao.close()


def put_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("update alunos set nome=%s, idade=%s where id=%s", (input("Digite o nome: "), int(input("Digite a idade: ")), int(input("Digite id: "))))
    conexao.commit()

    print("Aluno atualizado!")
    cursor.close()
    conexao.close()

@app.route("/alunos/<int:id>", methods=["PUT"])
def put_aluno(id):
    dados=request.json
    nome=dados["nome"]
    idade=dados["idade"]
    
    conexao=conectar()
    cursor=conexao.cursor()

    sql="UPDATE alunos SET nome=%s, idade=%s WHERE id=%s"
    cursor.execute(sql, (nome, idade, id))
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    return  jsonify({"mensagem": "Aluno atualizado"})

def delete_aluno():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("delete from alunos where id=%s", (int(input("Digite o id do aluno: ")),))
    conexao.commit()

    print('Aluno deletado!')
    cursor.close()
    conexao.close()



@app.route("/deletar")
def delete_alunos(id):
    conexao=conectar()
    cursor=conexao.cursor()

    
    cursor.execute("DELETE from aluno WHERE id=%s", (id))
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    return  redirect("/")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome=request.form["nome"]
    idade=request.form["idade"]
    conexao=conectar()
    cursor=conexao.cursor()

    sql="insert into alunos(nome, idade) values (%s, %s)"
    cursor.execute(sql, (nome,idade))
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    return  redirect("/")

if __name__ == "__main__":
    app.run(debug=True)