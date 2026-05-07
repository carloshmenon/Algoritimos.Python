import mysql.connector 
from db import conectar
#transformar em api flask
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/alunos", methods = ["GET"])
def get_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("select * from alunos")
    dados = cursor.fetchall()

    alunos = []
    for aluno in dados:
        alunos.append({
                "id": aluno[0],
                "nome": aluno[1],
                "idade": aluno[2]
            })
        #print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}")
    
    cursor.close()
    conexao.close()

    return jsonify(alunos)

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


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/alunos/<int:id>", methods=["DELETE"])
def delete_alunos(id):
    dados=request.json
    id=dados["id"]
    
    conexao=conectar()
    cursor=conexao.cursor()

    sql="DELETE from aluno WHERE id=%s"
    cursor.execute(sql, (id))
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    return  jsonify({"mensagem": "Aluno atualizado"})

@app.route("/alunos/", methods=["POST"])

def POST_alunos(nome, idade,id):
    dados=request.json
    nome=dados["nome"]
    idade=dados["idade"]
    id=dados["id"]
    
    conexao=conectar()
    cursor=conexao.cursor()

    sql="insert into alunos(nome, idade,id) values (%s, %s,%s)",(input("Digite o nome: "), int(input("Digite a idade: ")), int(input("Digite id: ")))
    cursor.execute(sql, (nome,idade,id))
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    return  jsonify({"mensagem": "Aluno atualizado"})