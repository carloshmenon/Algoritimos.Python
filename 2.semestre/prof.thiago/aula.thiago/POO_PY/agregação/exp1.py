

class Aluno:
    def __init__ (self, nome, ra):
        self.nome=nome
        self.ra=ra

class Universidade:
    def __init__ (self, nome):
        self.nome=nome
        self.alunos=[] #listas de alunos que frequentam a universidade

    def adicionar_aluno(self, aluno:object):
        self.alunos.append(aluno) 

    def lista_alunos(self): #aqui crio uma def para chamar sempre o print
        for item in self.alunos:
            print(f"nome:  {item.nome} | ra: {item.ra} ")

a1=Aluno("carlos","1234")# preenchendo a class aluno
a2=Aluno("tesman","4321")
a3=Aluno("fabio","4567")
a4=Aluno("gerson","1235")

faculdade= Universidade("SENAC MS")
print(len(faculdade.alunos))

faculdade.adicionar_aluno(a1)#adicionando alunos a lista self.alunos[]
faculdade.adicionar_aluno(a2)
faculdade.adicionar_aluno(a3)
faculdade.adicionar_aluno(a4)

print ("alunos da : ", faculdade.nome)
for aluno in faculdade.alunos:
    print(aluno.nome)

faculdade.lista_alunos()#aqui eu chamo a def que criei