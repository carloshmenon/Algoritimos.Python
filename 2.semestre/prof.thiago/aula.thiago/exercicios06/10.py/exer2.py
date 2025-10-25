
# Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes atributos:
# Nome
# Autor
# Editora
# Páginas
# A classe deve ter o seguintes métodos:
# Alterar_editora()
# Listar_qtde_paginas()

class Livros:
    def __init__ (self, nome, Autor, Editora, Paginas):
        self.nome=nome
        self.autor=Autor
        self.editora=Editora
        self.paginas=Paginas

    def name(self):
        print(f"nome do livro é {self.nome}")

    def pag(self):
        print(f"paginas total {self.paginas}")

    def aut(self):
        print(f"o autor do livro é {self.autor}")

    def edit(self):
        print(f"a editora desse livro é {self.editora}")

    def Alterar_editora(self, nova_editora):
        self.editora=nova_editora
        print(f"editora atualiazada, {self.editora} ")

    def mostrar(self):
        print(f"📖 Nome: {self.nome}")
        print(f"👤 Autor: {self.autor}")
        print(f"🏢 Editora: {self.editora}")
        print(f"📄 Páginas: {self.paginas}")

biblioteca=Livros("A caçada", "Carlos", "editora carlão", "530 paginas")

biblioteca.mostrar()