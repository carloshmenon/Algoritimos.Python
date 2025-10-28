
import mysql.connector

class database:
    def __ini__(self, banco = "perkal2") -> None:
        self.banco=banco
        self.host = "localhost"
        self.user= "root"

    def connect (self):
        self.conn = mysql.connector.connect(host=self.host ,database=self.banco,user="root",password="")
        if self.conn.is_connected():
            self.cursor= self.conn.cursor()
            db_info=self.conn.get_server_info()
            print ("CONECTADO COM SUCESSO")

        else:
            print("erroooo")

data=database()
data.connect()


