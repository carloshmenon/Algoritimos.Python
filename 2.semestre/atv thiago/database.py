import mysql.connector

class Database:
    def __init__(self, banco="restaurante_db") -> None:
        self.banco = banco
        self.host = "localhost"
        self.user = "root"
        self.password = "1234"  # ajuste conforme sua senha

    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            database=self.banco,
            user=self.user,
            password=self.password
        )
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            print("✅ CONECTADO COM SUCESSO")
        else:
            print("❌ ERRO NA CONEXÃO")

    def insert_garcom(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO garcom (nome) VALUES (%s)", tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def insert_produto(self, tupla):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO produto (nome, preco) VALUES (%s, %s)", tupla)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def insert_pedido(self, garcom_id):
        self.connect()
        try:
            self.cursor.execute("INSERT INTO pedido (garcom_id) VALUES (%s)", (garcom_id,))
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def select_all(self, tabela):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM {tabela}")
            result = self.cursor.fetchall()
            return result
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def select_by_id(self, tabela, id_coluna, id_valor):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM {tabela} WHERE {id_coluna} = %s", (id_valor,))
            result = self.cursor.fetchone()
            return result
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def update_garcom(self, tupla):
        self.connect()
        try:
            self.cursor.execute("""
                UPDATE garcom
                SET nome = %s
                WHERE id = %s
            """, (tupla[1], tupla[0]))
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def update_produto(self, tupla):
        self.connect()
        try:
            self.cursor.execute("""
                UPDATE produto
                SET nome = %s, preco = %s
                WHERE id = %s
            """, (tupla[1], tupla[2], tupla[0]))
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def delete_by_id(self, tabela, id_coluna, id_valor):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM {tabela} WHERE {id_coluna} = %s", (id_valor,))
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
        finally:
            self.close_connection()

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("🔒 Conexão encerrada com sucesso!")

# Teste rápido
if __name__ == "__main__":
    db = Database()
    db.connect()
