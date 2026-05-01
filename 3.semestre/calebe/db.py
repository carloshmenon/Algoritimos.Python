
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