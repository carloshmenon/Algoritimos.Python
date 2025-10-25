import mysql.connector 

class Database:
    def __init__(self, banco ="perkal") -> None:
        self.banco=banco 
        self.host="localhost"
        self.user="root"

    def connect (self):
        self.conn = mysql.connector.connect(host=self.host ,database=self.banco,user="root",password="")
        if self.conn.is_connected():
            self.cursor= self.conn.cursor()
            db_info=self.conn.get_server_info()
            print ("CONECTADO COM SUCESSO")

        else:
            print("erroooo")

    def insert(self,tupla):
        self.connect()
        
        try:
            self.cursor.execute("INSERT INTO cliente (nome,cpf,fone,cidade) VALUES (%s,%s,%s,%s)",tupla)
            self.conn.commit()
            return True
            
        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select(self):
        self.connect()
        try:
            self.cursor.execute(f"SELECT *FROM cliente")
            result=self.cursor.fetchall()
            return result

        except Exception as err:
            print (err)

        finally:
            self.close_connection()

    def select_by_id (self,id):
        self.connect()
        try:
            self.cursor.execute (f"SELECT*FROM cliente WHERE id_cli = {id}")
            result =self.cursor.fatchone()
            return result


        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update(self):
        self.connect()
        tupla= (2,"yann")
        try :
            self.cursor.execute(f"""UPDATE cliente SET nome= '{tupla[1]}' WHERE id_cli = {tupla[0]}""")
            self.conn.commit()
            return True
        except Exception as err:
            print (err)

        finally:
            self.close_connection()

    def delete(self,id_cli):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id_cli = {id_cli}")
            self.conn.commit()
            return True
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()


    def close_connection (self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("conexao encerrada com sucesso!!")

db = Database()
db.connect()
dados= ("gersooooo","123","456","campo grande")
cadastro= db.insert(dados)
delete= db.delete(5)#aqui deletamos o cliente id 5

if cadastro == True:
    print("Cadastro com sucesso!!")

if delete == True:
    print("deletado com sucesso")

db=Database()
dados=db.select()

for cliente in dados:
    print (f"id : {cliente[0]} | nome: {cliente[1]} | CPF : {cliente[2]} | fone : {cliente[3]} | cidade {cliente[4]}")

db=Database ()
dados= db.select_by_id(2)

print (dados)

