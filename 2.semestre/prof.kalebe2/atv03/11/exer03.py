
lista_de_alunos = []

class Aluno:
    def __init__(self, matricula, nome, n1, n2, n3):
        self.nome = nome
        self.matricula = matricula
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.n3 = float(n3)

    def cal_media(self):
        return (self.n1 + self.n2 + self.n3) / 3

def add_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    n1 = input("Digite a nota 1 do aluno: ")
    n2 = input("Digite a nota 2 do aluno: ")
    n3 = input("Digite a nota 3 do aluno: ")
    return Aluno(matricula, nome, n1, n2, n3)


for i in range(5):
    print(f"\nAluno {i+1}:")
    aluno_add = add_aluno()
    lista_de_alunos.append(aluno_add)


maior_media = -1
menor_media = 11
aluno_maior = None
aluno_menor = None

for aluno in lista_de_alunos:
    media = aluno.cal_media()
    print(f"{aluno.nome} - Média: {media:.2f}")

    if media > maior_media:
        maior_media = media
        aluno_maior = aluno

    if media < menor_media:
        menor_media = media
        aluno_menor = aluno

    if media >= 6:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")

print(f"\nAluno com maior média: {aluno_maior.nome} - {maior_media:.2f}")
print(f"Aluno com menor média: {aluno_menor.nome} - {menor_media:.2f}")


     
    
    
        