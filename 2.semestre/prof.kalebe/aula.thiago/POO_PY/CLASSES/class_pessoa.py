#herança

class Pessoa: #Super class 
    def __init__(self, nome, email, senha ):
        self.name = nome
        self.mail = email
        self.password = senha

    def hello(self):
        print (f" helloooo {self.name}")

#student está herdando a class pessoa

class Student (Pessoa):
    def __init__ (self, nome,email,senha, ra):
        super(). __init__ (nome, email, senha)
        self.ra =ra

p1=Pessoa("luis", "lulu@gmail.com", "123456") #aqui colocamos em ordem os atributos da class pessoa

p1.hello()

s1=Student("tesman", "tesman@gmail.com", "1234556","46587")
s1.hello() #hello vem da super class