
# Crie uma classe que modele um aluno. Esta classe deve possuir os seguintes atributos:
# Nome;
# RA;
# Nota 1, nota 2, nota 3, nota 4;
# A classe deve ter o seguintes método:
# Mostrar_situacao: (APROVADO / EXAME / REPROVADO). Considere que, nesse caso, a média final é calculada pela média aritmética simples de todas as notas e que o aluno é aprovado somente se obtiver média maior ou igual a sete. Exame entre 5 e 6.9. Reprovado abaixo de 5
# A situação será retornada a partir das notas obtidas pelo aluno.

class Aluno:
    def __init__ (self, nome, RA, N1, N2, N3, N4):
        self.nome=nome
        self.RA=RA
        self.N1=N1
        self.N2=N2
        self.N3=N3
        self.N4=N4

    def calcular_media (self):
            return (self.N1+self.N2+self.N3+self.N4)/4

media= Aluno("carlos","RA 123456", 10,5,10,8) 

resultado=media.calcular_media()

if resultado<5:
    print("aluno reprovado")

else:
     print("aluno aprovado")




        