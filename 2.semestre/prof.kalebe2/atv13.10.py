

class aluno:
    def __init__(self,nome, matricula):
        self.nome=nome
        self.matricula=matricula

class disciplina:
    def __init__(self, nomeDis, Cod_dis):
        self.disciplina=nomeDis
        self.codigo= Cod_dis

class Notas:
    def __init__(self,nota):
        self.nota=nota

a1= aluno("carlos","1234")
Disciplina=disciplina("programação", "2345")

nota_carlos=Notas(aluno=a1, disciplina=Disciplina, valor_nota=8.5)

print(nota_carlos)