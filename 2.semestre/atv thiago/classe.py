from database import Database

class Garcom:
    def __init__(self, nome=None):
        self.nome = nome

    def cadastrar(self):
        db = Database()
        tupla = (self.nome,)
        return db.insert_garcom(tupla)

    def buscar(self):
        db = Database()
        return db.select_all("garcom")

    def buscar_por_id(self, id):
        db = Database()
        return db.select_by_id("garcom", "id", id)

    def atualizar(self, tupla):
        db = Database()
        return db.update_garcom(tupla)

    def deletar(self, id):
        db = Database()
        return db.delete_by_id("garcom", "id", id)


class Produto:
    def __init__(self, nome=None, preco=0.0):
        self.nome = nome
        self.preco = preco

    def cadastrar(self):
        db = Database()
        tupla = (self.nome, self.preco)
        return db.insert_produto(tupla)

    def buscar(self):
        db = Database()
        return db.select_all("produto")

    def buscar_por_id(self, id):
        db = Database()
        return db.select_by_id("produto", "id", id)

    def atualizar(self, tupla):
        db = Database()
        return db.update_produto(tupla)

    def deletar(self, id):
        db = Database()
        return db.delete_by_id("produto", "id", id)


class Pedido:
    def __init__(self, garcom_id=None):
        self.garcom_id = garcom_id

    def cadastrar(self):
        db = Database()
        return db.insert_pedido(self.garcom_id)

    def buscar(self):
        db = Database()
        return db.select_all("pedido")

    def buscar_por_id(self, id):
        db = Database()
        return db.select_by_id("pedido", "id", id)

    def deletar(self, id):
        db = Database()
        return db.delete_by_id("pedido", "id", id)
