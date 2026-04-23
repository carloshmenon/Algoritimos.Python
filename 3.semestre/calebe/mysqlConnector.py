import mysql.connector

#criar conexao
conexao=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
if conexao.is_connected():
    print("conectado com sucesso")
#responsavel por executar os comandos sql
# conexao.cursor().execute()
cursor=conexao.cursor()


cursor.execute("create database if not exists aula_connect")

conexao.database="aula_connect"

cursor.execute("show databases")
#mostrar os bancos criados
for banco in cursor.fetchall():
    print(banco)

cursor.execute(
    """ create table if not exists alunos(id int primary key auto_increment,
    nome varchar(100) not null, idade int
    )"""
)

#comando insert
sql="insert into alunos(nome,idade) values(%s,%s)"
valores=("tesmaCarlos",24 )
cursor.execute(sql,valores)
conexao.commit()#para as informacoes add irem para o banco

#executar consulta
cursor.execute("select * from alunos")
resultados= cursor.fetchall()
for linha in resultados:
    print(linha)

#fechar cursor e conexao

cursor.close()
conexao.close()